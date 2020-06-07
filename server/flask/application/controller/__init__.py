from flask.views import MethodView
from flask       import request, abort
from typing      import List
from ..          import db

# fix delete for conviction

class BaseAPI(MethodView):

    model  : db.Model
    name   : str
    fields : List[str]
    foreign: List[db.Model]
    backref: str

    def query(self, id, model=None):
        row = (model if model else self.model).query.get(id)
        if not row: abort(404)
        return row

    def append(self, row, id, model):
        if id:
            parent = self.query(id, model)
            getattr(parent, self.backref).append(row)

    def set_request_fields(self, row):
        req = request.json.get

        if getattr(self, 'fields', None):
            for field in self.fields: 
                if req(field): setattr(row, field, req(field))
        else:
            if req(self.name): setattr(row, self.name, req(self.name))

        if getattr(self, 'foreign', None):
            for model in self.foreign:
                self.append(row, req(model.__tablename__), model)

        db.session.add(row)
        db.session.commit()
        return self.query(row.id).get_dict()

    def get(self, id):
        if id: return self.query(id).get_dict()

        all_rows = {self.name: []}
        for each in self.model.query.all():
            all_rows[self.name].append(each.get_dict())
        return all_rows

    def post(self):
        return self.set_request_fields(self.model())

    def put(self, id):
        return self.set_request_fields(self.query(id))

    def delete(self, id):
        db.session.delete(self.query(id))
        db.session.commit()
        return {'id': id}


def base_rule(bp, api):
    view = api.as_view(f"{api.name}_api")

    bp.add_url_rule(f'/{api.name}/', defaults={'id': None}, 
        methods=['GET'], view_func=view)
    bp.add_url_rule(f'/{api.name}', 
        methods=['POST'], view_func=view)
    bp.add_url_rule(f'/{api.name}/<int:id>', 
        methods=['GET', 'PUT', 'DELETE'], view_func=view)

# products = Product.query.paginate(page, 10).items
from flask.views import MethodView
from flask       import request, abort
from ..          import db

class BaseAPI(MethodView):

    name : str
    model: db.Model

    def query(self, id, model=None):
        record = (model if model else self.model).query.get(id)
        if not record: abort(404)
        return record

    def get(self, id):
        if id: return self.query(id).get_dict()

        all_records = {self.name: []}
        for each in self.model.query.all():
            all_records[self.name].append(each.get_dict())
        return all_records

    def post(self):
        record = self.model(request.json.get(self.name))
        db.session.commit()
        return record.get_dict()

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
# db.session.add(record)
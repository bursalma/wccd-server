from flask.views import MethodView
from flask       import request, abort
from ..          import db

class BaseAPI(MethodView):

    def __init__(self):
        self.name  = None
        self.model = None

    def get(self, id):
        if id: 
            try:
                return self.model.query.get(id).get_dict()
            except AttributeError:
                abort(404)

        all_records = {self.name: []}
        
        for each in self.model.query.all():
            all_records[self.name].append(each.get_dict())

        return all_records

    def post(self):
        record = self.model(request.json.get(self.name))

        db.session.add(record)
        db.session.commit()
        return record.get_dict()

    def delete(self, id):
        db.session.delete(self.model.query.get(id))
        db.session.commit()
        return {'id': id}


def base_rule(bp, api, endpoint):
    view = api.as_view(f"{endpoint}_api")

    bp.add_url_rule(
        f'/{endpoint}/', 
        defaults={'id': None},
        view_func=view, 
        methods=['GET'])
    bp.add_url_rule(
        f'/{endpoint}', 
        view_func=view, 
        methods=['POST'])
    bp.add_url_rule(
        f'/{endpoint}/<int:id>', 
        view_func=view,
        methods=['GET', 'PUT', 'DELETE'])

# products = Product.query.paginate(page, 10).items
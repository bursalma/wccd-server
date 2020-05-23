from flask.views import MethodView

class BaseAPI(MethodView):
    def __init__(self):
        self.name  = None
        self.model = None

    def get(self, id):
        if id: return self.model.query.get(id).get_dict()

        all_records = {self.name: []}
        
        for each in self.model.query.all():
            all_records[self.name].append(each.get_dict())

        return all_records

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



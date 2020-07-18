from typing import Dict, List, Union

from flask import abort, request
from flask.views import MethodView

from .. import db


class BaseAPI(MethodView):
    """Base API class to configure default http methods for all endpoints."""

    model: db.Model

    def query(self, id: int, model: db.Model = None) -> object:
        row = (model if model else self.model).query.get(id)
        if not row:
            abort(404)
        return row

    def set_request_fields(self, row: object) -> Dict[str, Union[str, int]]:
        try:
            req = request.json.get
        except AttributeError:
            abort(404)

        for field in self.model.fields():
            if field[-3:] == '_id':
                model = self.model.models()[field[:-3].title()]
                id = req(model.__tablename__ + '_id')

                if id:
                    parent = self.query(id, model)
                    backref = f'all_{self.model.__tablename__}'
                    getattr(parent, backref).append(row)
            else:
                if req(field):
                    try:
                        setattr(row, field, req(field))
                    except AttributeError:
                        abort(404)

        db.session.add(row)
        db.session.commit()
        return self.query(row.id).get_dict()

    def get(self, id: int) -> Dict[str, Union[Union[str, int], List[dict]]]:
        """Get row by id or get all."""
        if id:
            return self.query(id).get_dict()

        all_rows = {self.model.__tablename__: []}
        for each in self.model.query.all():
            all_rows[self.model.__tablename__].append(each.get_dict())
        return all_rows

    def post(self: int) -> Dict[str, Union[str, int]]:
        return self.set_request_fields(self.model())

    def put(self, id: int) -> Dict[str, Union[str, int]]:
        return self.set_request_fields(self.query(id))

    def delete(self, id: int) -> Dict[str, int]:
        db.session.delete(self.query(id))
        db.session.commit()
        return {'id': id}


def base_rule(bp: object, api: MethodView):
    """Configure default routing for all endpoints."""
    name = api.model.__tablename__
    view = api.as_view(f"{name}_api")

    bp.add_url_rule(f'/{name}/', defaults={'id': None},
                    methods=['GET'], view_func=view)
    bp.add_url_rule(f'/{name}',
                    methods=['POST'], view_func=view)
    bp.add_url_rule(f'/{name}/<int:id>',
                    methods=['GET', 'PUT', 'DELETE'], view_func=view)

# products = Product.query.paginate(page, 10).items

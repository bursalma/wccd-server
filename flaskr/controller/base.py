from typing import Dict, List, Union

from flask import abort, request
from flask.views import MethodView

from .. import db


class BaseAPI(MethodView):
    """Base API class configures default http methods for all endpoints."""

    #: The following attributes represent parameters unique to each API
    model: db.Model
    name: str
    fields: List[str]
    foreign: List[db.Model]
    backref: str

    def query(self, id: int, model: object = None) -> object:
        row = (model if model else self.model).query.get(id)
        if not row:
            abort(404)
        return row

    def append(self, row: object, id: int, model: object) -> None:
        if id:
            parent = self.query(id, model)
            getattr(parent, self.backref).append(row)

    def set_request_fields(self, row: object) -> Dict[str, Union[str, int]]:
        req = request.json.get

        if getattr(self, 'fields', None):
            for field in self.fields:
                if req(field):
                    setattr(row, field, req(field))
        else:
            if req(self.name):
                setattr(row, self.name, req(self.name))

        if getattr(self, 'foreign', None):
            for model in self.foreign:
                self.append(row, req(model.__tablename__), model)

        db.session.add(row)
        db.session.commit()
        return self.query(row.id).get_dict()

    def get(self, id: int) -> Dict[str, Union[Union[str, int], List[dict]]]:
        """Get row by id or get all."""
        if id:
            return self.query(id).get_dict()

        all_rows = {self.name: []}
        for each in self.model.query.all():
            all_rows[self.name].append(each.get_dict())
        return all_rows

    def post(self: int) -> Dict[str, Union[str, int]]:
        return self.set_request_fields(self.model())

    def put(self, id: int) -> Dict[str, Union[str, int]]:
        return self.set_request_fields(self.query(id))

    def delete(self, id: int) -> Dict[str, int]:
        db.session.delete(self.query(id))
        db.session.commit()
        return {'id': id}


def base_rule(bp: object, api: MethodView) -> None:
    """Configure default routing for all endpoints."""
    view = api.as_view(f"{api.name}_api")

    bp.add_url_rule(f'/{api.name}/', defaults={'id': None},
                    methods=['GET'], view_func=view)
    bp.add_url_rule(f'/{api.name}',
                    methods=['POST'], view_func=view)
    bp.add_url_rule(f'/{api.name}/<int:id>',
                    methods=['GET', 'PUT', 'DELETE'], view_func=view)

# products = Product.query.paginate(page, 10).items

from flask import Blueprint, request, abort
from .     import BaseAPI, base_rule
from ..    import db
from ..model.nationality import Nationality

nationality_bp = Blueprint('nationality_bp', __name__)

class NationalityAPI(BaseAPI):

    model = Nationality
    name  = Nationality.__tablename__

    def put(self, id):
        req = request.json.get
        row = self.query(id)

        if req(self.name): row.nationality = req(self.name)

        row_dict = row.get_dict()
        db.session.commit()
        return row_dict

base_rule(nationality_bp, NationalityAPI)
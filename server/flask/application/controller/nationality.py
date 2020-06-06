from flask               import Blueprint, request, abort
from .                   import BaseAPI, base_rule
from ..                  import db
from ..model.nationality import Nationality

nationality_bp = Blueprint('nationality_bp', __name__)

class NationalityAPI(BaseAPI):

    model = Nationality
    name  = Nationality.__tablename__

    def put(self, id):
        req    = request.json.get
        record = self.query(id)

        if req(self.name): record.nationality = req(self.name)

        db.session.commit()
        return record.get_dict()

base_rule(nationality_bp, NationalityAPI)
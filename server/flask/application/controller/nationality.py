from flask               import Blueprint, request
from .                   import BaseAPI, base_rule
from ..                  import db
from ..model.nationality import Nationality

nationality_bp = Blueprint('nationality_bp', __name__)

class NationalityAPI(BaseAPI):

    def __init__(self):
        self.name  = 'nationality'
        self.model = Nationality

    def put(self, id):
        record = self.model.query.get(id)
        val    = request.json.get(self.name)

        if val: record.nationality = val #fix this

        db.session.commit()
        return record.get_dict()

base_rule(nationality_bp, NationalityAPI, 'nationality')
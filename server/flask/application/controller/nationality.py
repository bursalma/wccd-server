from flask       import Blueprint, request
from flask.views import MethodView

from .                   import base_rule, BaseAPI
from ..                  import db
from ..model.nationality import Nationality

nationality_bp = Blueprint('nationality_bp', __name__)

class NationalityAPI(BaseAPI):

    def __init__(self):
        self.name  = 'nationality'
        self.model = Nationality

    def post(self):
        body = request.json.get

        nationality = Nationality(body('nationality'))

        db.session.add(nationality)
        db.session.commit()
        return nationality.get_dict()

    def delete(self, id):
        db.session.delete(Nationality.query.get(id))
        db.session.commit()
        return {'id': id}

    def put(self, id):
        nationality = Nationality.query.get(id)
        body        = request.json.get

        if body('nationality'): nationality.nationality = body('nationality')

        db.session.commit()
        return nationality.get_dict()

base_rule(nationality_bp, NationalityAPI, 'nationality')
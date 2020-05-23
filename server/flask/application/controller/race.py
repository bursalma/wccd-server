from flask       import Blueprint, request
from flask.views import MethodView

from .            import base_rule, BaseAPI
from ..           import db
from ..model.race import Race

race_bp = Blueprint('race_bp', __name__)

class RaceAPI(BaseAPI):

    def __init__(self):
        self.name  = 'race'
        self.model = Race

    def post(self):
        race = Race(request.json.get('race'))

        db.session.add(race)
        db.session.commit()
        return race.get_dict()

    def delete(self, id):
        db.session.delete(Race.query.get(id))
        db.session.commit()
        return {'id': id}

    def put(self, id):
        race = Race.query.get(id)
        val  = request.json.get('race')

        if val: race.race = val

        db.session.commit()
        return race.get_dict()

base_rule(race_bp, RaceAPI, 'race')
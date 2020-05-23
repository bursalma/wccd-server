from flask        import Blueprint, request
from .            import BaseAPI, base_rule
from ..           import db
from ..model.race import Race

race_bp = Blueprint('race_bp', __name__)

class RaceAPI(BaseAPI):

    def __init__(self):
        self.name  = 'race'
        self.model = Race

    def put(self, id):
        record = self.model.query.get(id)
        val    = request.json.get(self.name)

        if val: record.race = val #fix this

        db.session.commit()
        return record.get_dict()

base_rule(race_bp, RaceAPI, 'race')
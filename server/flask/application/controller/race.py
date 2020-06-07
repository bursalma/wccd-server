from flask import Blueprint, request
from .     import BaseAPI, base_rule
from ..    import db
from ..model.race import Race

race_bp = Blueprint('race_bp', __name__)

class RaceAPI(BaseAPI):

    model = Race
    name  = Race.__tablename__

    def put(self, id):
        req = request.json.get
        row = self.query(id)

        if req(self.name): row.race = req(self.name)

        row_dict = row.get_dict()
        db.session.commit()
        return row_dict

base_rule(race_bp, RaceAPI)
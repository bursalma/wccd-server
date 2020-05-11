from flask       import Blueprint, request
from flask.views import MethodView

from ..                  import db
from ..models.race        import Race
from ..models.convict     import Convict

race_bp = Blueprint('race_bp', __name__)

class RaceAPI(MethodView):

    def get(self, race_id):
        if race_id != None:
            return Race.query.get(race_id).get_dict()

        all_races = {'races': []}
        
        for each_race in Race.query.all():
            all_races['races'].append(each_race.get_dict())

        return all_races

race_view = RaceAPI.as_view("race_api")
race_bp.add_url_rule(
    '/race/', 
    defaults={'race_id': None},
    view_func=race_view, 
    methods=['GET'])
race_bp.add_url_rule('/race/<int:race_id>', 
    view_func=race_view,
    methods=['GET'])
from flask       import Blueprint, request
from flask.views import MethodView

from ..                  import db
from ..model.race        import Race
from ..model.convict     import Convict

race_bp = Blueprint('race_bp', __name__)

class RaceAPI(MethodView):

    def get(self, race):
        if race != None:
            race = Race.query.filter_by(race=race).first()
            return race.get_dict()
            # return {'race': race.race, 'children': race.get_children()}
            # return Race.query.get(race).get_dict()


        all_races = {'races': []}
        
        for each_race in Race.query.all():
            # all_races['races'].append({'race': each_race.race, 'children': each_race.get_children()})
            all_races['races'].append(each_race.get_dict())

        return all_races

race_view = RaceAPI.as_view("race_api")
race_bp.add_url_rule(
    '/race/', 
    defaults={'race': None},
    view_func=race_view, 
    methods=['GET'])
race_bp.add_url_rule('/race/<race>', 
    view_func=race_view,
    methods=['GET'])
from flask       import Blueprint, request
from flask.views import MethodView

from ..                   import db
from ..model.nationality import Nationality
from ..model.convict     import Convict

nationality_bp = Blueprint('nationality_bp', __name__)

class NationalityAPI(MethodView):

    def get(self, nationality_id):
        if nationality_id != None:
            return Nationality.query.get(nationality_id).get_dict()

        all_nationalities = {'nationalities': []}
        
        for each_nationality in Nationality.query.all():
            all_nationalities['nationalities'].append(each_nationality.get_dict())

        return all_nationalities

nationality_view = NationalityAPI.as_view("nationality_api")
nationality_bp.add_url_rule(
    '/nationality/', 
    defaults={'nationality_id': None},
    view_func=nationality_view, 
    methods=['GET'])
nationality_bp.add_url_rule('/nationality/<int:nationality_id>', 
    view_func=nationality_view,
    methods=['GET'])
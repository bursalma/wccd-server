from flask       import Blueprint, request, jsonify, make_response
from flask.views import MethodView

from .                   import base_rule, BaseAPI
from ..                  import db
from ..model.convict     import Convict
from ..model.race        import Race
from ..model.nationality import Nationality

convict_bp = Blueprint('convict_bp', __name__)

class ConvictAPI(BaseAPI):

    def __init__(self):
        self.name  = 'convict'
        self.model = Convict
            
    def post(self):
        body = request.json.get

        convict = Convict(body('last_name'), body('first_name'), body('middle_name'), body('sex'))

        race = Race.query.get(body('race'))
        race.convicts.append(convict)

        nationality = Nationality.query.get(body('nationality'))
        nationality.convicts.append(convict)

        db.session.add(convict)
        db.session.commit()
        return convict.get_dict()

    def delete(self, id):
        db.session.delete(Convict.query.get(id))
        db.session.commit()
        return {'id': id}

    def put(self, id):
        convict = Convict.query.get(id)
        body    = request.json.get

        if body('last_name')  : convict.last_name   = body('last_name')
        if body('first_name') : convict.first_name  = body('first_name')
        if body('middle_name'): convict.middle_name = body('middle_name')
        if body('sex')        : convict.sex         = body('sex')

        if body('race'): 
            race = Race.query.get(body('race'))
            race.convicts.append(convict)

        if body('nationality'): 
            nationality = Nationality.query.get(body('nationality'))
            nationality.convicts.append(convict)

        db.session.commit()
        return convict.get_dict()

base_rule(convict_bp, ConvictAPI, 'convict')
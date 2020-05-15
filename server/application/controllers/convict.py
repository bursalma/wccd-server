from flask       import Blueprint, request, jsonify, make_response
from flask.views import MethodView

from ..                   import db
from ..models.convict     import Convict
from ..models.race        import Race
from ..models.nationality import Nationality

convict_bp = Blueprint('convict_bp', __name__)

class ConvictAPI(MethodView):

    def get(self, convict_id):
        if convict_id != None:
            return Convict.query.get(convict_id).get_dict()

        all_convicts = {'convicts': []}
        
        for each_convict in Convict.query.all():
            all_convicts['convicts'].append(each_convict.get_dict())

        return all_convicts
            
    def post(self):
        body = request.json.get

        last_name  = body('last_name')
        first_name = body('first_name')

        if not last_name or not first_name:
            unmet_response = {
                'error'  : 'requirements unmet',
                'message': 'last_name and first_name fields are required'}
            return unmet_response, 404

        existing_convict = Convict.query.filter(
            Convict.last_name == last_name).filter(
            Convict.first_name == first_name).first()

        if existing_convict:
            exists_response = {
                'error'  : 'record exists',
                'message': f'{last_name}, {first_name} already exists'}
            return exists_response, 404

        new_convict = Convict(last_name, first_name, body('middle_name'), body('sex'))

        race = Race.query.filter_by(race=body('race')).first()
        if race == None: race = Race(body('race'))
        race.convicts.append(new_convict)

        nationality = Nationality.query.filter_by(nationality=body('nationality')).first()
        if nationality == None: nationality = Nationality(body('nationality'))
        nationality.convicts.append(new_convict)

        db.session.add(new_convict)
        db.session.commit()
        return new_convict.get_dict()

    def delete(self, convict_id):
        db.session.delete(Convict.query.get(convict_id))
        db.session.commit()
        return {'id': convict_id}

    def put(self, convict_id):
        convict = Convict.query.get(convict_id)
        body    = request.json.get

        if body('last_name')  : convict.last_name   = body('last_name')
        if body('first_name') : convict.first_name  = body('first_name')
        if body('middle_name'): convict.middle_name = body('middle_name')
        if body('sex')        : convict.sex         = body('sex')

        if body('race'): 
            race = Race.query.filter_by(race=body('race')).first()
            if race == None: race = Race(body('race'))
            race.convicts.append(convict)

        if body('nationality'): 
            nationality = Nationality.query.filter_by(nationality=body('nationality')).first()
            if nationality == None: nationality = Nationality(body('nationality'))
            nationality.convicts.append(convict)

        db.session.commit()
        return convict.get_dict()

convict_view = ConvictAPI.as_view("convict_api")
convict_bp.add_url_rule(
    '/convict/', 
    defaults={'convict_id': None},
    view_func=convict_view, 
    methods=['GET'])
convict_bp.add_url_rule(
    '/convict', 
    view_func=convict_view, 
    methods=['POST'])
convict_bp.add_url_rule('/convict/<int:convict_id>', 
    view_func=convict_view,
    methods=['GET', 'PUT', 'DELETE'])

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404
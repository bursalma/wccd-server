from flask       import Blueprint, request, jsonify, make_response, abort
from flask.views import MethodView
from .                   import base_rule, BaseAPI
from ..                  import db
from ..model.convict     import Convict
from ..model.race        import Race
from ..model.nationality import Nationality

convict_bp = Blueprint('convict_bp', __name__)

class ConvictAPI(BaseAPI):
    
    model = Convict
    name  = Convict.__tablename__

    def append(self, record, req, model):
        if req(model.__tablename__):
            parent = self.query(req(model.__tablename__), model)
            parent.convicts.append(record)
            
    def post(self):
        req    = request.json.get
        record = Convict(req('last_name'),   req('first_name'), 
                         req('middle_name'), req('sex'))

        self.append(record, req, Race)
        self.append(record, req, Nationality)

        db.session.commit()
        return record.get_dict()

    def put(self, id):
        req    = request.json.get
        record = self.query(id)

        if req('last_name')  : record.last_name   = req('last_name')
        if req('first_name') : record.first_name  = req('first_name')
        if req('middle_name'): record.middle_name = req('middle_name')
        if req('sex')        : record.sex         = req('sex')

        self.append(record, req, Race)
        self.append(record, req, Nationality)

        db.session.commit()
        return record.get_dict()

base_rule(convict_bp, ConvictAPI)
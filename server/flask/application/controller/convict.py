from flask       import Blueprint, request, abort
from flask.views import MethodView
from .           import base_rule, BaseAPI
from ..          import db
from ..model.convict     import Convict
from ..model.race        import Race
from ..model.nationality import Nationality

convict_bp = Blueprint('convict_bp', __name__)

class ConvictAPI(BaseAPI):
    
    model = Convict
    name  = Convict.__tablename__

    def append(self, row, req, model):
        if req(model.__tablename__):
            parent = self.query(req(model.__tablename__), model)
            parent.convicts.append(row)
            
    def post(self):
        req = request.json.get
        row = Convict(
            last_name   = req('last_name'),
            first_name  = req('first_name'), 
            middle_name = req('middle_name'), 
            sex         = req('sex'))

        self.append(row, req, Race)
        self.append(row, req, Nationality)

        db.session.add(row)
        db.session.commit()
        return self.query(row.id).get_dict()

    def put(self, id):
        req = request.json.get
        row = self.query(id)

        if req('last_name')  : row.last_name   = req('last_name')
        if req('first_name') : row.first_name  = req('first_name')
        if req('middle_name'): row.middle_name = req('middle_name')
        if req('sex')        : row.sex         = req('sex')

        self.append(row, req, Race)
        self.append(row, req, Nationality)

        db.session.commit()
        return self.query(row.id).get_dict()

base_rule(convict_bp, ConvictAPI)
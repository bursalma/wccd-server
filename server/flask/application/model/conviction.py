# from .        import BaseModel
# from ..       import db
# from typing   import Dict, Union
# from datetime import datetime

# now = datetime.utcnow

# class Conviction(db.Model, BaseModel):

#     __tablename__ = 'conviction'
#     id          = db.Column(db.Integer, primary_key=True)
#     age_group   = db.Column(db.String(20))
#     company     = db.Column(db.String(85))
#     affiliation = db.Column(db.Boolean)
#     charges     = db.Column(db.Integer)
#     court_type  = db.Column(db.String(20))
#     sentence    = db.Column(db.Integer)
#     fine        = db.Column(db.Integer)
#     decade      = db.Column(db.String(20))
#     parole      = db.Column(db.Boolean)
#     summary     = db.Column(db.String(950))
#     source_name = db.Column(db.String(85))
#     source_url  = db.Column(db.String(200))
#     source_date = db.Column(db.DateTime)
#     last_update = db.Column(db.DateTime, default=now, onupdate=now)
    
#     convict_id = db.Column(db.Integer, db.ForeignKey('convict.id'))

#     # def __init__(self, last_name, first_name, middle_name, sex):
#     #     self.last_name   = last_name
#     #     self.first_name  = first_name
#     #     self.middle_name = middle_name
#     #     self.sex         = sex

#     # def get_dict(self) -> Dict[str, Union[str, int]]:
#     #     return {
#     #         'id'         : self.id,
#     #         'last_name'  : self.last_name,
#     #         'first_name' : self.first_name,
#     #         'middle_name': self.middle_name,
#     #         'sex'        : self.sex,
#     #         'race'       : self.race_id,
#     #         'nationality': self.nationality_id
#     #     }
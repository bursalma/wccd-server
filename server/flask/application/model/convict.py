from .  import BaseModel
from .. import db
from datetime import datetime

now = datetime.utcnow

class Convict(db.Model, BaseModel):

    __tablename__ = 'convict'
    id          = db.Column(db.Integer, primary_key=True)
    last_name   = db.Column(db.String(45))
    first_name  = db.Column(db.String(45))
    middle_name = db.Column(db.String(45))
    sex         = db.Column(db.String(10))
    last_update = db.Column(db.DateTime, default=now, onupdate=now)
    
    race_id        = db.Column(db.Integer, db.ForeignKey('race.id'))
    nationality_id = db.Column(db.Integer, db.ForeignKey('nationality.id'))

    def __init__(self, last_name, first_name, middle_name, sex):
        self.last_name   = last_name
        self.first_name  = first_name
        self.middle_name = middle_name
        self.sex         = sex

    def __repr__(self):
        return f'<Convict {self.last_name}, {self.first_name}>'

    def get_dict(self):
        return {
            'id'         : self.id,
            'last_name'  : self.last_name,
            'first_name' : self.first_name,
            'middle_name': self.middle_name,
            'sex'        : self.sex,
            'race'       : self.race.id,
            'nationality': self.nationality.id
        }
from .. import db
from datetime import datetime

now = datetime.utcnow

class Race(db.Model):

    __tablename__ = 'race'
    id          = db.Column(db.Integer, primary_key=True)
    race        = db.Column(db.String(20))
    last_update = db.Column(db.DateTime, default=now, onupdate=now)
    convicts    = db.relationship('Convict', backref='race')

    def __init__(self, race):
        self.race = race

    def __repr__(self):
        return f'<Race {self.race}>'

    def get_dict(self):
        return {
            'id'  : self.id,
            'race': self.race 
        }
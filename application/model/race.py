from datetime import datetime

from . import BaseModel
from .. import db

now = datetime.utcnow


class Race(db.Model, BaseModel):
    __tablename__ = 'race'
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(20))
    last_update = db.Column(db.DateTime, default=now, onupdate=now)
    convicts = db.relationship('Convict', backref='race')

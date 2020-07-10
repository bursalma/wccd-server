from datetime import datetime

from . import BaseModel
from .. import db

now = datetime.utcnow


class Sector(db.Model, BaseModel):
    __tablename__ = 'sector'
    id = db.Column(db.Integer, primary_key=True)
    sector = db.Column(db.String(85))
    sector_desc = db.Column(db.String(85))
    last_update = db.Column(db.DateTime, default=now, onupdate=now)

    # race_id     = db.Column(db.Integer, db.ForeignKey('race.id'))
    # nationality_id = db.Column(db.Integer, db.ForeignKey('nationality.id'))
    # convictions = db.relationship('Conviction', backref='convict')

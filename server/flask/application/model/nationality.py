from .        import BaseModel
from ..       import db
from datetime import datetime

now = datetime.utcnow

class Nationality(db.Model, BaseModel):

    __tablename__ = 'nationality'
    id          = db.Column(db.Integer, primary_key=True)
    nationality = db.Column(db.String(45))
    last_update = db.Column(db.DateTime, default=now, onupdate=now)
    convicts    = db.relationship('Convict', backref='nationality')
from .base import BaseModel, db, now


class Convict(db.Model, BaseModel):
    __tablename__ = 'convict'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(45))
    first_name = db.Column(db.String(45))
    middle_name = db.Column(db.String(45))
    sex = db.Column(db.String(10))
    last_update = db.Column(db.DateTime, default=now, onupdate=now)
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'))
    nationality_id = db.Column(db.Integer, db.ForeignKey('nationality.id'))
    all_conviction = db.relationship('Conviction', backref='convict')

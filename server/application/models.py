from . import db
from datetime import datetime


class Race(db.Model):

    __tablename__ = 'race'
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(20), unique=True, nullable=False)
    last_update = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, race):
        self.race = race

    def __repr__(self):
        return '<Race {}>'.format(self.race)


class Nationality(db.Model):

    __tablename__ = 'nationality'
    id = db.Column(db.Integer, primary_key=True)
    nationality = db.Column(db.String(45), unique=True, nullable=False)
    last_update = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, nationality):
        self.nationality = nationality

    def __repr__(self):
        return '<Nationality {}>'.format(self.nationality)

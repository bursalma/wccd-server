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


class Convict(db.Model):

    __tablename__ = 'convict'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(45))
    first_name = db.Column(db.String(45))
    middle_name = db.Column(db.String(45))
    sex = db.Column(db.ENUM('male', 'female', name='sex'))
    race_id = None
    nationality_id = None
    last_update = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, last_name, first_name, middle_name, sex):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.sex = sex

    def __repr__(self):
        return '<Convict {}>'.format(self.convict)

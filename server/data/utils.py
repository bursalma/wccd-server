"""Module to insert initial data after the creation of the tables."""
from csv import reader

from .. import db
from ..model.nationality import Nationality
from ..model.race import Race
from ..model.sector import Sector


def basic_insert(model: db.Model, data: list):
    """Insert given data to the given table."""
    for item in data:
        row = model()
        setattr(row, row.__tablename__, item)
        db.session.add(row)
    db.session.commit()


def txt_list(file: str) -> list:
    """Read txt from data directory."""
    with open('server/data/' + file) as f:
        return [row.replace('\n', '') for row in f]


def dynamic_insert(model: db.Model, file: str):
    """Dynamically add to table using first line for fields"""
    fields = []
    first_line = True
    with open('server/data/' + file) as f:
        for line in reader(f):
            if first_line:
                fields = line
                first_line = False
            else:
                row = model()
                for i, val in enumerate(line):
                    if val != '':
                        setattr(row, fields[i], val)
                db.session.add(row)
        db.session.commit()


def initial_insert():
    """Used by application init at the start of the server."""
    basic_insert(Nationality, txt_list('nationality.txt'))
    basic_insert(Race, ['Asian', 'Black', 'Hispanic',
                        'White', 'Other', 'NOT REPORTED'])
    dynamic_insert(Sector, 'sector.csv')

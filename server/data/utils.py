"""Module to insert initial data after the creation of the tables."""
from csv import reader

from .. import db
from ..model.nationality import Nationality
from ..model.race import Race


def base_insert(model: db.Model, data: list):
    """Insert given data to the given table."""
    for item in data:
        row = model()
        setattr(row, row.__tablename__, item)
        db.session.add(row)
    db.session.commit()


def txt_data(file: str) -> list:
    """Read txt from data directory."""
    with open('server/data/' + file) as f:
        return [row.replace('\n', '') for row in f]


# def csv_data(file: str) -> list:
#     """Read yaml from data directory."""
#     with open('server/data/' + file) as f:
#         for row in reader(f):
#             return row

    # with open('server/data/' + file) as f:
    #     return safe_load(f)


def initial_insert():
    """Used by application init at the start of the server."""
    base_insert(Nationality, txt_data('nationalities.txt'))
    base_insert(Race, ['Asian', 'Black', 'Hispanic',
                       'White', 'Other', 'NOT REPORTED'])

    # with open('server/data/test.json') as f:
    #     import json
    #     dat = json.load(f)
    #     print(type(dat))
    #     print(dat)

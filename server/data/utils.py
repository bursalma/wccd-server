"""Module to insert initial data after the creation of the tables."""
from typing import List

from yaml import safe_load

from .. import db
from ..model.nationality import Nationality
from ..model.race import Race


def base_insert(model: db.Model, data: List[str]) -> None:
    """Insert given data to the given table."""
    for item in data:
        row = model()
        setattr(row, row.__tablename__, item)
        db.session.add(row)
    db.session.commit()


def data(file: str) -> List[str]:
    """Read yaml from data directory."""
    with open('server/data/' + file) as f:
        return safe_load(f)


def initial_insert() -> None:
    """Used by application init at the start of the server."""
    base_insert(Nationality, data('nationalities.yaml'))
    base_insert(Race, ['Asian', 'Black', 'Hispanic',
                       'White', 'Other', 'NOT REPORTED'])

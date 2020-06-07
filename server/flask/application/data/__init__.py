from yaml import safe_load as yaml_safe_load
from ..                  import db
from ..model.race        import Race
from ..model.nationality import Nationality

def base_insert(model, data):
    for item in data:
        row = model()
        setattr(row, row.__tablename__, item)
        db.session.add(row)
    db.session.commit()


def data(file):
    with open('application/data/' + file) as f: 
        return yaml_safe_load(f)
     

def initial_insert():
    base_insert(Race, ['Asian', 'Black', 'Hispanic', 'White', 'Other', 'NOT REPORTED'])
    base_insert(Nationality, data('nationalities.yaml'))
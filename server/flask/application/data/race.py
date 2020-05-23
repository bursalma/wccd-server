from .            import base_insert
from ..model.race import Race

def initial_insert():
    races = ['Asian', 'Black', 'Hispanic', 'White', 'Other', 'NOT REPORTED']

    base_insert(races, Race)
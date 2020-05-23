from flask import url_for

from ..controller.race import RaceAPI

def insert_race():

    races = ['Asian', 'Black', 'Hispanic', 'White', 'Other', 'NOT REPORTED']
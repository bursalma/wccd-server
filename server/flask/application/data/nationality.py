from .                   import base_insert
from ..model.nationality import Nationality

def initial_insert():
    data = ['American', 'Turkish', 'Other', 'NOT REPORTED']

    base_insert(data, Nationality)
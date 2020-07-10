from flask import Blueprint

from . import BaseAPI, base_rule
from ..model.race import Race

race_bp = Blueprint('race_bp', __name__)


class RaceAPI(BaseAPI):
    model = Race
    name = Race.__tablename__


base_rule(race_bp, RaceAPI)

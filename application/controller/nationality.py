from flask import Blueprint

from . import BaseAPI, base_rule
from ..model.nationality import Nationality

nationality_bp = Blueprint('nationality_bp', __name__)


class NationalityAPI(BaseAPI):
    model = Nationality
    name = Nationality.__tablename__
    # print(Nationality.metadata.__dict__)


base_rule(nationality_bp, NationalityAPI)

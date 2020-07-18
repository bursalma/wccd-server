from flask import Blueprint

from .base import BaseAPI, base_rule
from ..model.nationality import Nationality

nationality_bp = Blueprint('nationality_bp', __name__)


class NationalityAPI(BaseAPI):
    model = Nationality


base_rule(nationality_bp, NationalityAPI)

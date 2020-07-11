from flask import Blueprint

from .base import BaseAPI, base_rule
from ..model.convict import Convict
from ..model.nationality import Nationality
from ..model.race import Race

convict_bp = Blueprint('convict_bp', __name__)


class ConvictAPI(BaseAPI):
    model = Convict
    name = Convict.__tablename__
    fields = ['last_name', 'first_name', 'middle_name', 'sex']
    foreign = [Race, Nationality]
    backref = 'convicts'


base_rule(convict_bp, ConvictAPI)

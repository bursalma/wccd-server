from flask import Blueprint

from .base import BaseAPI, base_rule
from ..model.convict import Convict

convict_bp = Blueprint('convict_bp', __name__)


class ConvictAPI(BaseAPI):
    model = Convict


base_rule(convict_bp, ConvictAPI)

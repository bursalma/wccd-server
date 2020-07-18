from flask import Blueprint

from .base import BaseAPI, base_rule
from ..model.conviction import Conviction

conviction_bp = Blueprint('conviction_bp', __name__)


class ConvictionAPI(BaseAPI):
    model = Conviction


base_rule(conviction_bp, ConvictionAPI)

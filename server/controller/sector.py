from flask import Blueprint

from .base import BaseAPI, base_rule
from ..model.sector import Sector, SectorConviction

sector_bp = Blueprint('sector_bp', __name__)
sector_conviction_bp = Blueprint('sector_conviction_bp', __name__)


class SectorAPI(BaseAPI):
    model = Sector


class SectorConvictionAPI(BaseAPI):
    model = SectorConviction


base_rule(sector_bp, SectorAPI)
base_rule(sector_conviction_bp, SectorConvictionAPI)

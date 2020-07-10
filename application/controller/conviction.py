from flask import Blueprint

from . import BaseAPI, base_rule
from application.model.conviction import Conviction
from application.model.convict import Convict

conviction_bp = Blueprint('conviction_bp', __name__)


class ConvictionAPI(BaseAPI):
    model = Conviction
    name = Conviction.__tablename__
    fields = ['age_group', 'company', 'affiliation', 'charges', 'court_type',
              'sentence', 'fine', 'decade', 'parole', 'summary', 'source_name',
              'source_url', 'source_date']
    foreign = [Convict]
    backref = 'convictions'


base_rule(conviction_bp, ConvictionAPI)

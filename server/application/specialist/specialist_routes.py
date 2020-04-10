from flask import Blueprint, render_template

# Set up a Blueprint
specialist_bp = Blueprint('specialist_bp', __name__)


@specialist_bp.route('/specialist', methods=['GET'])
def specialist():
    return 'hi, you are a specialist'
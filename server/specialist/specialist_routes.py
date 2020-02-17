from flask import Blueprint, render_template
from flask import current_app as app


# Set up a Blueprint
specialist_bp = Blueprint('specialist_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@specialist_bp.route('/specialist', methods=['GET'])
def specialist():
    return 'hi, you are a specialist'
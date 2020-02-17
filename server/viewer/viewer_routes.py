from flask import Blueprint, render_template
from flask import current_app as app


# Set up a Blueprint
viewer_bp = Blueprint('viewer_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@viewer_bp.route('/viewer', methods=['GET'])
def viewer():
    return 'hi, you are a viewer'
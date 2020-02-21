from flask import Blueprint, render_template

# Set up a Blueprint
viewer_bp = Blueprint('viewer_bp', __name__)


@viewer_bp.route('/viewer', methods=['GET'])
def viewer():
    return 'hi, you are a viewer'
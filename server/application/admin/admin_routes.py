from flask import Blueprint, render_template

# Set up a Blueprint
admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route('/admin', methods=['GET'])
def admin():
    """Admin page route."""
    return 'hi, you are an admin'
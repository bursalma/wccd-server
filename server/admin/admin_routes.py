from flask import Blueprint, render_template
from flask import current_app as app


# Set up a Blueprint
admin_bp = Blueprint('admin_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@admin_bp.route('/admin', methods=['GET'])
def admin():
    """Admin page route."""
    return 'hi, you are an admin' #render_template('admin.html')
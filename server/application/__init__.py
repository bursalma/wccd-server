from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

db = SQLAlchemy()


def create_app():

    app = Flask(__name__, instance_relative_config=False)
    load_dotenv()
    app.config.from_object('config.DevConfig')
    db.init_app(app)

    with app.app_context():

        from .              import routes
        from .admin         import admin_routes
        from .specialist    import specialist_routes
        from .viewer        import viewer_routes

        app.register_blueprint(routes.main_bp)
        app.register_blueprint(admin_routes.admin_bp)
        app.register_blueprint(specialist_routes.specialist_bp)
        app.register_blueprint(viewer_routes.viewer_bp)

        # Create tables for our models
        db.create_all()

        return app
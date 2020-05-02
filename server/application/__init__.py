from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, getcwd

db = SQLAlchemy()

# FLASK_APP="wsgi:create_app('prod')"
def create_app():

    app = Flask(__name__, instance_relative_config=False)

    # app.config.from_object('config.DevConfig')

    app.config.from_object('config.ProdConfig')

    print(app.config)
    
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

        db.create_all()

        return app
from os import environ

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)

    # if environ.get('FLASK_ENV') == 'development':
    #     app.config.from_object('config.DevConfig')
    # else:
    #     app.config.from_object('config.ProdConfig')

    app.config.from_object('config.DevConfig')
    db.init_app(app)

    with app.app_context():
        from .controller import race, nationality, convict, \
                                conviction
        from .data import initial_insert

        app.register_blueprint(race.race_bp)
        app.register_blueprint(nationality.nationality_bp)
        app.register_blueprint(convict.convict_bp)
        app.register_blueprint(conviction.conviction_bp)

        db.create_all()
        initial_insert()
        return app

# def common(app):
#     @app.errorhandler(404)
#     def not_found(error):
#         return {'hi':'hey'}, 404

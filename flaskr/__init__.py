from os import environ

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(env='prod'):
    app = Flask(__name__, instance_relative_config=False)

    if env == 'dev':
        app.config.from_object('config.DevConfig')
    else:
        app.config.from_object('config.ProdConfig')

    db.init_app(app)

    with app.app_context():
        from .controller import race, nationality, convict, \
                                conviction
        from .data.utils import initial_insert

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

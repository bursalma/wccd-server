from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ

db = SQLAlchemy()

def create_app():

    app = Flask(__name__, instance_relative_config=False)

    # app.config.from_object('config.DevConfig')

    if environ.get('FLASK_ENV') == 'development':
        app.config.from_object('config.DevConfig')
    else:
        app.config.from_object('config.ProdConfig')
    
    db.init_app(app)

    with app.app_context():

        from .controller import convict, race, nationality

        app.register_blueprint(convict.convict_bp)
        app.register_blueprint(race.race_bp)
        app.register_blueprint(nationality.nationality_bp)

        db.create_all()

        return app
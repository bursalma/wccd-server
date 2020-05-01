"""Flask config class."""
from os import environ


class Config:
    """Set Flask configuration vars from .env file."""
    # FLASK_APP = environ.get('FLASK_APP')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    # FLASK_RUN_PORT=8080


class ProdConfig(Config):
    FLASK_ENV = environ.get('PROD_FLASK_ENV')
    DEBUG = False
    TESTING    = False
    SECRET_KEY = environ.get('PROD_SECRET_KEY')
    SESSION_COOKIE_NAME     = environ.get('PROD_SESSION_COOKIE_NAME')
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    # FLASK_ENV = environ.get('DEV_FLASK_ENV')
    DEBUG = True
    TESTING    = True
    SECRET_KEY = environ.get('DEV_SECRET_KEY')
    SESSION_COOKIE_NAME     = environ.get('DEV_SESSION_COOKIE_NAME')
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI')
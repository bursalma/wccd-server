"""Flask config class."""
from os import environ

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    """Set Flask configuration vars from .env file."""
    SECRET_KEY = environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME     = environ.get('SESSION_COOKIE_NAME')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')


class DevConfig(Config):
    SECRET_KEY = '_5#y2L"F4Q8z\n\xec]/'
    SESSION_COOKIE_NAME     = 'white_collar_flask_dev_cookie'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
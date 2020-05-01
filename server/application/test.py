from dotenv import load_dotenv
from os import environ, path, getcwd
env_path = path.dirname(getcwd()) + '/.env.prod'
print(env_path)
load_dotenv(dotenv_path=env_path)
load_dotenv()
print(environ.get('SQLALCHEMY_TRACK_MODIFICATIONS'))
print(environ.get('PROD_FLASK_ENV'))
print(environ.get('PROD_DATABASE_URI'))
print(environ.get('DEV_DATABASE_URI'))
print(environ.get('DEV_FLASK_ENV'))

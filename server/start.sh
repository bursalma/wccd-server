# start.sh

cd server
pipenv shell
pipenv update
export FLASK_APP=wsgi.py
export FLASK_ENV=development
# export APP_CONFIG_FILE=config.py
flask run
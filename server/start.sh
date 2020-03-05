# start.sh

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=wsgi.py
export FLASK_ENV=development
# export APP_CONFIG_FILE=config.py
flask run
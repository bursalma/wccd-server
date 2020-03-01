# start.ps1

pipenv shell
pipenv update
$env:FLASK_APP="wsgi.py"
$env:FLASK_ENV="development"
# $env:APP_CONFIG_FILE="config.py"
flask run
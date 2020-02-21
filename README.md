# White-Collar
Repository to develop the white-collar database app

## Running the Client
Navigate to the client folder and install the node modules:
`cd client && npm install`

Start the client:
`npm start` or `yarn start`

## Running the Server ##
go to server folder and make sure pipenv is installed
unix: `pip3 install pipenv`
win : `pip install pipenv`

start pipenv virtual environment
`cd client && pipenv shell`

install required packages from the pipfile
`pipenv install`

set flask server
unix: `export FLASK_APP="wsgi.py"`
cmd : `set FLASK_APP="wsgi.py"`
ps  : `$env:FLASK_APP="wsgi.py"`

optionally turn on debug mode for deploying changes during service
unix: `export FLASK_ENV="development"`
cmd : `set FLASK_ENV="development"`
ps  : `$env:FLASK_ENV="development"`

run
`flask run`

pending
`export APP_CONFIG_FILE="config.py"`
`$env:APP_CONFIG_FILE="config.py"`
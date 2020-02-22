# White-Collar
Repository to develop the white-collar database app

## Running the Client
Navigate to the client folder and install the node modules:
`cd client && npm install`

Start the client:
`npm start` or `yarn start`

## Running the Server ##
#### make sure pipenv is installed
    pip3 install pipenv

#### start pipenv virtual environment
    cd server && pipenv shell

#### install required packages from the pipfile
    pipenv update

#### set flask server
```sh
export FLASK_APP=wsgi.py
$env:FLASK_APP="wsgi.py"
```

##### optionally turn on debug mode for deploying changes during service
```sh
export FLASK_ENV=development
$env:FLASK_ENV="development"
```

#### run
    flask run

#### ignore me
```sh
export APP_CONFIG_FILE="config.py"
$env:APP_CONFIG_FILE="config.py"
```
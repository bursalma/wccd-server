# White-Collar
Repository to develop the white-collar database app

## Running the Client
Navigate to the client folder and install the node modules:
`cd client && npm install`

Start the client:
`npm start` or `yarn start`

## Running the Server
```sh
cd server
python3 -m venv venv #first time only
. venv/bin/activate
pip3 install -r requirements.txt
export FLASK_ENV=development #for debug mode
export FLASK_APP="wsgi:create_app('dev')" #for dev
flask run
pip3 freeze > requirements.txt #if made updates
```
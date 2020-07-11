# White-Collar
Repository to develop the white-collar crime database app

## Running the Server
```sh
python3 -m venv venv #first time only
. venv/bin/activate #source venv/Scripts/activate
pip3 install -r requirements.txt
flask run
pip3 freeze > requirements.txt #if made updates
```
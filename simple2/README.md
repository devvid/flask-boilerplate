# flask-boilerplate-simple2
Simple Flask project 2; Basic Flask app with DB & model support using SQLAlchmey 

## Important
Make sure to generate a new secret key in the `src/config.py` file.

## Install
Run the following code block before starting up the app for the first time.
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=src
flask db init
flask db migrate -m "init"
flask db upgrade
flask run
```
### Test Data
Once setup; Inject test data into the database using the following command
(venv)`python seed.py`

## Run
Start script
```
. venv/bin/activate
export FLASK_APP=src
flask run
```
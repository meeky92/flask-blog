# import the flask class from the flask module
from flask import Flask
# import SQALCHEMY and Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# import the Config class from the config module
from config import Config

# create an instance of the Flask class and give it the variable name 'app'
app = Flask(__name__)
# if templates folder named something else, can insert here after __name__, template_folder = 'abc'

# add a SECRET_KEY to the app config
app.config.from_object(Config)

# create an instance of SQLAlchemy to represent our database
db = SQLAlchemy(app)

# create an instance of migrate to represent our migration engine
migrate = Migrate(app, db)

# import all the routes and models from the routes module in the current folder
from . import routes, models
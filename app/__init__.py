# import the flask class from the flask module
from flask import Flask

# create an instance of the Flask class and give it the variable name 'app'
app = Flask(__name__)
# if templates folder named something else, can insert here after __name__, template_folder = 'abc'

# add a SECRET_KEY to the app config
app.config['SECRET_KEY'] = 'you-will-never-guess'

# import all the routes from the routes module in the current folder
from . import routes
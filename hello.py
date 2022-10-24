# import the flask class from the flask module
from flask import Flask

# create an instance of the Flask class and give it the variable name 'app'
app = Flask(__name__)

# create a route using the @app.route to trigger function based on endpoint
@app.route('/')
def index():
    return 'Hello this is the index route!'


# run the application
# if __name__ == '__main__':
#     app.run()

# add another route
@app.route('/posts')
def posts():
    return 'Posts will eventually be on this page'
from flask import render_template, redirect, url_for
from app import app
from app.forms import SignUpForm

# create a route using the @app.route to trigger function based on endpoint
@app.route('/')
def index():
    user_info = {
        'username': 'eunicek',
        'email': 'eunicek@ct.com'
    }
    colors = ['red', 'orange', 'yellow', 'blue', 'indigo', 'violet']
    return render_template('index.html', user = user_info, colors = colors)

# run the application
# if __name__ == '__main__':
#     app.run()

# add another route
@app.route('/posts')
def posts():
    return 'Posts will eventually be on this page'

@app.route('/signup', methods = ["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('Hooray our form submitted!')
        # get data from form 
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(email, username, password)
        # add a new user to the database

        # redirect back to hoem
        return redirect(url_for('index'))
    return render_template('signup.html', form = form)
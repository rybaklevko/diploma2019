from app import app
from flask import render_template
import templates

@app.route('/', methods=['GET'])
def start_page():
    is_registered = False

    if (is_registered):
        # user sign in (if registered)
        # get user from db
        # if exists - log in
        return log_in_page()
    else:
        # user registration
        return registration()


@app.route('/registration', methods=['GET'])
def registration():
    return render_template('signup.html')


@app.route('/sign_in', methods=['GET'])
def log_in_page():
    return render_template("login.html")

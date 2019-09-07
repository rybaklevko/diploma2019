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
        return log_user_in()
    else:
        # user registration
        return log_in_page()


@app.route("/log_user_in", methods=['POST','GET'])
def log_user_in():
    #check is user in database
    #if yes, open user page
    #if no, shows an error and ask to register
    return "User page"



@app.route("/register_user", methods=['POST','GET'])
def register_user():
    #1)add user into db

    #2)log in
    return log_user_in()



@app.route('/profile_page', methods=['GET'])
def profile_page():
    return render_template("profile.html")


@app.route('/log_in_page', methods=['GET'])
def log_in_page():
    return render_template("login.html")


@app.route('/registration_page', methods=['POST','GET'])
def registration_page():
    return render_template('signup.html')



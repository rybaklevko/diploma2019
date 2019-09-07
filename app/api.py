from app import app
from flask import render_template, Response, request
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


@app.route("/log_user_in", methods=['POST', 'GET'])
def log_user_in():
    print("LOG USER IN!")
    #check is user in database
    #if yes, open user page
    #if no, shows an error and ask to register

    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        print(username+password)
        #response = get_user_from_db(username, password);
        #status_code = response.status_code


        status_code = 400
        if (username == "admin@admin"):
            if (password == "admin123"):
                status_code = 200



        if status_code == 200:
            return user_main_page()
        else:
            return "ERROR"

    else:
        return "Not post request!"


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


@app.route('/user_main_page', methods=['POST','GET'])
def user_main_page():
    return render_template('user_main_page.html')

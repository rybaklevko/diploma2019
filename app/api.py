from app import app
from flask import request

from pages import login_page, registration_page, devices_page


@app.route('/', methods=['GET'])
def start_page():
    is_registered = False

    if is_registered:
        # user sign in (if registered)
        # get user from db
        # if exists - log in
        return log_user_in()
    else:
        # user registration
        return login_page.log_in_page()


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


        if username == '' or password == '':
            error = "Both user name and password are required!"
            return login_page.log_in_page(error)

        #response = get_user_from_db(username, password);
        #status_code = response.status_code

        status_code = 400
        if username == "admin@admin":
            if password == "admin123":
                status_code = 200

        if status_code == 200:
            return devices_page.devices_page()
        else:
            error="User's credentials are wrong!"
            return login_page.log_in_page(error)

    else:
        return "Not post request!"


@app.route("/register_user", methods=['POST', 'GET'])
def register_user():

    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        print(email + name + password)


        if email == '' or password == '' or name == '':
            error = "All these fields are required!"
            return registration_page.registration_page(error)

            #1)add user into db

            # #2)log in
            return log_user_in()

    else:
        return "Not post request!"


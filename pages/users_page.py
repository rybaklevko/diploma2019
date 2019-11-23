from app import app
from flask import render_template


# TODO data for device have to be read from DataBase
users_list = [{'firstName': 'Roman', 'secondName': 'Savuch', 'imagesList':{'jeff1.jpg','jeff2.jpg','jeff3.jpg'}},
              {'firstName': 'Lev', 'secondName': 'Rybak', 'imagesList': {'lev1.jpg', 'lev2.jpg', 'lev3.jpg'}}]


@app.route('/add_user', methods=['POST'])
def add_devices(error=''):
    # add user, read from requests form and add into users_list

    return users_page(error)


@app.route('/users_page', methods=['GET', 'POST'])
def users_page(error=''):
    return render_template("users.html", users=users_list, error=error)
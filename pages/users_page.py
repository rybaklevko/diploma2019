from app import app
from flask import render_template


# TODO data for device have to be read from DataBase
users_list = [{'firstName': 'Lev', 'secondName': 'Rybak', 'imagesList':{'lev1.jpg','lev2.jpg','lev3.jpg'}}]
    #,               {'firstName': 'Oleg', 'secondName': 'Pronko'}]

@app.route('/users_page', methods=['GET', 'POST'])
def users_page(error=''):
    return render_template("users.html", users=users_list, error=error)
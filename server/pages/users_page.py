from app import app
from flask import render_template

import base64
from PIL import Image
from io import BytesIO

# TODO data for device have to be read from DataBase
users_list = [{'firstName': 'Roman', 'secondName': 'Savuch', 'imagesList': {'jeff1.jpg','jeff2.jpg','jeff3.jpg'}},
               {'firstName': 'Lev', 'secondName': 'Rybak', 'imagesList': {'lev1.jpg', 'lev2.jpg', 'lev3.jpg'}}]


@app.route('/add_user', methods=['POST'])
def add_new_user(error=''):
    # add user, read from requests form and add into users_list

    return render_template("users.html", users=users_list, error=error)


@app.route('/users_page', methods=['GET', 'POST'])
def users_page(error=''):
    with open("C:\\Users\\Lev\\PycharmProjects\\face_recognition_lock_server\\server\\DB\\images\\lev1.jpg", "rb") as image_file:
        img = base64.b64encode(image_file.read()).decode('ascii')
    return render_template("users.html", users=users_list, img_data=img, error=error)
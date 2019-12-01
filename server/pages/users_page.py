from app import app
from flask import render_template, redirect

import base64
from PIL import Image
from io import BytesIO

# TODO data for device have to be read from DataBase
users_list = [{'user_id':'1','firstName': 'Roman', 'secondName': 'Savuch', 'imagesList': {'rom1.jpg','rom2.jpg','rom3.jpg'}},
               {'user_id':'2','firstName': 'Lev', 'secondName': 'Rybak', 'imagesList': {'lev1.jpg', 'lev2.jpg', 'lev3.jpg'}}]


class UserWebPage():
    def __init__(self, firstName="", secondName="", imageList={}):
        self.firstName = firstName
        self.secondName = secondName
        self.imageList = imageList

@app.route('/add_user', methods=['POST'])
def add_new_user(error=''):
    # add user, read from requests form and add into users_list

    return redirect('/users_page')#render_template("users.html", users=users_list, error=error)


@app.route('/users_page', methods=['GET', 'POST'])
def users_page(error=''):
    users = []
    for user in users_list:
        images = []
        images_name = []
        for image in user['imagesList']:
            file_name = "C:\\Users\\Lev\\PycharmProjects\\face_recognition_lock_server\\server\\DB\\images\\" + image
            with open(file_name, "rb") as image_file:
                images_name.append(file_name)
                img = base64.b64encode(image_file.read()).decode('ascii')
                images.append(img)

        users.append(UserWebPage(user['firstName'], user['secondName'], images))

    return render_template("users.html", users=users, error=error)
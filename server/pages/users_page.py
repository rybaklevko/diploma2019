from app import app
from flask import render_template, redirect, request

import base64, os
from werkzeug.utils import secure_filename

# TODO data for device have to be read from DataBase
users_list = [{'user_id':'1','firstName': 'Roman', 'secondName': 'Savuch', 'imagesList': {'rom1.jpg','rom2.jpg','rom3.jpg'}},
               {'user_id':'2','firstName': 'Lev', 'secondName': 'Rybak', 'imagesList': {'lev1.jpg', 'lev2.jpg', 'lev3.jpg'}}]


class UserWebPage():
    def __init__(self, firstName = "", secondName = "", imageList = {}):
        self.firstName = firstName
        self.secondName = secondName
        self.imageList = imageList


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/add_user', methods=['GET', 'POST'])
def add_user(error=''):
    # add user, read from requests form and add into users_list
    try:
        if request.method == 'POST':
            print("Is post method")
            if 'file' not in request.files:
                print('No file part')

            second_name = request.form["second_name"]
            first_name = request.form["first_name"]
            image_file = request.files["image_list"]

            if image_file.filename == '':
                print('No selected file')
            if image_file and allowed_file(image_file.filename):
                print(image_file.filename)
                filename = secure_filename(image_file.filename)
                full_path = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_file.save(full_path)

            user = dict()
            user['used_id'] = 3
            user['firstName'] = first_name
            user['secondName'] = second_name
            user['imagesList'] = []
            user['imagesList'].append(image_file.filename)

            users_list.append(user)
            return redirect('/users_page')
        else:
            print("Is not post method!!")
    except KeyError:
        print("No such key in form")

    return render_template("users_adding.html",  error=error)


@app.route('/users_page', methods=['GET', 'POST'])
def users_page(error=''):
    users = []
    for user in users_list:
        images = []
        images_name = []
        for image in user['imagesList']:
            file_name = (os.path.join(app.config['UPLOAD_FOLDER'], image))
            with open(file_name, "rb") as image_file:
                images_name.append(file_name)
                img = base64.b64encode(image_file.read()).decode('ascii')
                images.append(img)

        users.append(UserWebPage(user['firstName'], user['secondName'], images))

    return render_template("users.html", users=users, error=error)
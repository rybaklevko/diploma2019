from app import app
from flask import render_template, redirect, request

import base64, os
from werkzeug.utils import secure_filename

from app import mdls


class UserWebPage():
    def __init__(self, firstName = "", secondName = "", imageList = {}):
        self.firstName = firstName
        self.secondName = secondName
        self.imageList = imageList


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_image(image_file):
    if image_file.filename == '':
        print('No selected file')
    if image_file and allowed_file(image_file.filename):
        print(image_file.filename)
        filename = secure_filename(image_file.filename)
        full_path = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_file.save(full_path)

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
            image_files = []
            image_files.append(request.files["image1"])
            image_files.append(request.files["image2"])
            image_files.append(request.files["image3"])

            user = dict()
            user['used_id'] = 3
            user['firstName'] = first_name
            user['secondName'] = second_name
            user['imagesList'] = []
            for image_file in image_files:
                save_image(image_file)
                user['imagesList'].append(image_file.filename)

            mdls.users_list_models.append(user)
            #users_list.append(user)
            return redirect('/users_page')
        else:
            print("Is not post method!!")
    except KeyError:
        print("No such key in form")

    return render_template("users_adding.html",  error=error)


@app.route('/users_page', methods=['GET', 'POST'])
def users_page(error=''):
    users = []
    for user in mdls.users_list_models:
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
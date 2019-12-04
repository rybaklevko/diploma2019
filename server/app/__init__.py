#!/usr/bin/python3

from flask import Flask
UPLOAD_FOLDER = 'C:\\Users\\Lev\\PycharmProjects\\face_recognition_lock_server\\server\\DB\\images\\'
app = Flask(__name__, template_folder='../templates/', static_folder='../static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import api


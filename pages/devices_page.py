from app import app
from flask import render_template

# TODO data for device have to be read from DataBase
device_list = [{'name': 'rybak_device', 'ip': '2', 'userList': ['Lev Rybak', 'DSA dsa'], 'address' : 'Konovalsta str'}]


@app.route('/devices_page', methods=['GET', 'POST'])
def devices_page(error=''):
    return render_template("devices.html", devices=device_list, error=error)
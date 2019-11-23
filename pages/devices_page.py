from app import app
from flask import render_template

# TODO data for device have to be read from DataBase
device_list = [{'name': 'rybak_device', 'ip': '192.168.30.63', 'userList': {'Lev Rybak'}, 'address' : 'Konovalsta str'},
               {'name': 'pronko_device', 'ip': '192.168.30.213', 'userList': {'Prohnko Oleg'}, 'address': 'Naykova str'}]


@app.route('/add_device', methods=['POST'])
def add_devices(error=''):
    #add device, read from requests form and add into device_list

    return render_template("devices.html", devices=device_list, error=error)

@app.route('/devices_page', methods=['GET', 'POST'])
def devices_page(error=''):
    return render_template("devices.html", devices=device_list, error=error)
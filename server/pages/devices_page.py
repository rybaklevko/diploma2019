from app import app
from flask import render_template, redirect, request

# TODO data for device have to be read from DataBase
device_list = [{'device_id':'1','device_name': 'rybak_device', 'ip': '192.168.30.63', 'address' : 'Konovalsta str'},
               {'device_id':'2','device_name': 'pronko_device', 'ip': '192.168.30.213', 'address': 'Naykova str'}]


@app.route('/add_device', methods=['POST'])
def add_devices(error=''):
    #add device, read from requests form and add into device_list
    try:
        if request.method == 'POST':
            print("Is post method")
            device = dict()
            device['device_id'] = 3
            device['device_name'] = request.form["device_name"]
            device['ip'] = request.form["ip"]
            device['address'] = request.form["address"]

            device_list.append(device)
            return redirect('/devices_page')
        else:
            print("Is not post method!!")
    except KeyError:
        print("No such key in form")

    return render_template("device_adding.html",  error=error)


@app.route('/devices_page', methods=['GET', 'POST'])
def devices_page(error=''):
    return render_template("devices.html", devices=device_list, error=error)
from app import app
from flask import render_template


@app.route('/devices_page', methods=['GET', 'POST'])
def devices_page(error=''):
    return render_template("devices.html", error=error)
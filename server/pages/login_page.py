from app import app
from flask import render_template

@app.route('/log_in_page', methods=['GET'])
def log_in_page(error=''):
    return render_template("login.html", error=error)
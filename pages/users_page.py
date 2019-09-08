from app import app
from flask import render_template


@app.route('/users_page', methods=['GET', 'POST'])
def users_page(error=''):
    return render_template("users.html", error=error)
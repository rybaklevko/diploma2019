from app import app
from flask import render_template


@app.route('/app_info_page', methods=['GET', 'POST'])
def app_info_page(error=''):
    return render_template("app_info.html", error=error)
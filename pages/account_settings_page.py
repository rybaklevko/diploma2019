from app import app
from flask import render_template


@app.route('/account_settings_page', methods=['GET', 'POST'])
def account_settings_page(error=''):
    return render_template("account_settings.html", error=error)
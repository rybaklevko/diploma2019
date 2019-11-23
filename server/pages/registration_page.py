from app import app
from flask import render_template


@app.route('/registration_page', methods=['POST', 'GET'])
def registration_page(error=''):
    return render_template('signup.html', error=error)
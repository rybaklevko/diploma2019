from app import app
from flask import render_template


@app.route('/user_main_page', methods=['POST', 'GET'])
def user_main_page():
    return render_template('user_main_page.html')
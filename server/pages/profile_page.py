from app import app
from flask import render_template

@app.route('/profile_page', methods=['GET'])
def profile_page():
    return render_template("profile.html")

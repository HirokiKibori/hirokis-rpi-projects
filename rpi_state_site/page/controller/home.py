from flask import Blueprint, render_template
from datetime import datetime

home = Blueprint('home', __name__)
"""
flask-Blueprint for index-page (home-page)
"""


@home.route('/')
def index_site():
    """
    request-mapping for index-page (home-page)
    :return: rendered template for index-page
    """
    return render_template("home.html", time=datetime.now().strftime("%Y-%m-%d | %H:%M:%S"))
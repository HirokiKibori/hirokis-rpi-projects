from flask import Blueprint, render_template
from datetime import datetime

home = Blueprint('home', __name__)


@home.route('/')
def index_site():
    return render_template("home.html", time=datetime.now().strftime("%Y-%m-%d | %H:%M:%S"))
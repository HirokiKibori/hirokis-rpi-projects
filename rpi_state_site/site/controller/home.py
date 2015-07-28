from flask import Blueprint, render_template

home = Blueprint('home', __name__)


@home.route('/')
def index_site():
    return render_template("main_template.html")
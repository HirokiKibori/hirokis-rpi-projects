from flask import Blueprint, render_template
from page.util import command

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
    (out, err) = command.run_shell_command(["ipconfig"])
    return render_template("home.html", ip_information=out)
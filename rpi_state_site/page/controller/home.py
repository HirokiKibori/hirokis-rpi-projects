from flask import Blueprint, render_template
from page.util import command as shellcommand

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
    results = []

    from page import app
    if "INDEX_SHELL_COMMANDS" in app.config:
        for command in app.config['INDEX_SHELL_COMMANDS']:
            (out, err) = shellcommand.run_shell_command(command)
            if out is not None and out:
                results.append((command, out))
            if err is not None and err:
                app.logger.warning("run_shell_command -> %s:\n%s" % (command, err))

    return render_template("home.html", command_results=results)
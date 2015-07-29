from flask import Flask, render_template
from page.controller import home
from datetime import datetime


# instantiation for appliation-object
app = Flask(__name__)
app.config.from_pyfile('../config/configuration.py')


# request-mappings
@app.errorhandler(404)
def page_not_found(error):
    """
    request-mapping for 404 -> url not found
    a error-log will be add
    :param error: the error-string
    :return: rendered template for error-page
    """
    app.logger.error(error)
    return render_template('error_page_404.html', time=datetime.now().strftime("%Y-%m-%d | %H:%M:%S")), 404

app.register_blueprint(home.home)
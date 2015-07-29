from flask import Flask, render_template
from page.controller import home


app = Flask(__name__)
app.config.from_pyfile('../config/configuration.py')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_page_404.html'), 404

app.register_blueprint(home.home)
from flask import Flask
from page.controller import home


app = Flask(__name__)
app.config.from_pyfile('../config/configuration.py')

app.register_blueprint(home.home)
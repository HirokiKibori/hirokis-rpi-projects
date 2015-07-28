from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('main_template.html')


if __name__ == "__main__": 
    app.run(use_debugger=True, use_reloader=True, debug=True, host='0.0.0.0')


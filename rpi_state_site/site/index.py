from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return 'Server is running ... ^^'

if __name__ == "__main__": 
    app.run(use_debugger=True, use_reloader=True, debug=True, host='0.0.0.0')


from site import app

app.run(use_debugger=app.config["DEBUG"], use_reloader=app.config["DEBUG"], debug=app.config["DEBUG"], host='0.0.0.0')
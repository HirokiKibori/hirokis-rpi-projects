from page import app, logger

# set log_file_handler
logger.set_log_file_handler(app)


# Set configurations
app.logger.info('load configurations')
debug = False if "DEBUG" not in app.config else app.config['DEBUG']
host = '127.0.0.1' if "HOST" not in app.config else app.config['HOST']
port = 5000 if "PORT" not in app.config else app.config['PORT']


# Run app
app.logger.info('application starts')
app.run(use_debugger=debug, use_reloader=debug, debug=debug, host=host, port=port)
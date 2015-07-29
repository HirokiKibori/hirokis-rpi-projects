import logging
import os


# reset log_level and add log_handler
def set_log_file_handler(app, folder_path='logs'):
    if app is None:
        pass

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    info_file_handler = logging.FileHandler("%s%s" % (folder_path, '/info.log'))
    info_file_handler.setLevel(logging.INFO)

    debug_file_handler = logging.FileHandler("%s%s" % (folder_path, '/debug.log'))
    debug_file_handler.setLevel(logging.DEBUG)

    warning_file_handler = logging.FileHandler("%s%s" % (folder_path, '/warning.log'))
    warning_file_handler.setLevel(logging.WARNING)

    error_file_handler = logging.FileHandler("%s%s" % (folder_path, '/error.log'))
    error_file_handler.setLevel(logging.ERROR)

    defect_file_handler = logging.FileHandler("%s%s" % (folder_path, '/defect.log'))
    defect_file_handler.setLevel(logging.CRITICAL)

    app.logger.addHandler(info_file_handler)
    app.logger.addHandler(debug_file_handler)
    app.logger.addHandler(warning_file_handler)
    app.logger.addHandler(error_file_handler)
    app.logger.addHandler(defect_file_handler)

    app.logger.setLevel(logging.INFO)

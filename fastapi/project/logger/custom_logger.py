import logging
from logging.handlers import RotatingFileHandler

class CustomLogger:
    def __init__(self, log_file, log_level):
        self.logger = logging.getLogger(log_file)
        # handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('{"@timestamp": "%(asctime)s", "msg": %(message)s}')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(log_level)
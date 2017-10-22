# -*- coding: utf-8 -*-
import logging.handlers

# TODO: all bead but work. Must rewrite

LOG_FILENAME = "logs/ScriptMaster.log"
DEBUG_LEVEL = logging.DEBUG  # ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
LOG_FORMAT = "%(levelname)-8s [%(asctime)s] [%(thread)d : %(funcName)s] %(message)s"

logg = logging.getLogger('MyLogger')
logg.setLevel(DEBUG_LEVEL)

# logger rotate config
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=9000000, backupCount=5)
handler.setFormatter(logging.Formatter(LOG_FORMAT))

logg.addHandler(handler)

class log:

    def info(self, param):
        logg.info(param)

    def debug(self, param):
        logg.debug(param)

    def warn(self, param):
        logg.warn(param)

    def error(self, param):
        logg.error(param)

    def critical(self, param):
        logg.critical(param)






if __name__ == '__main__':
    print("hi")

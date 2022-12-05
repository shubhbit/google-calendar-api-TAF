import logging, os

class Logger(object):
    def __init__(self, name):
        if not os.path.exists("log"):
            os.makedirs("log")
        self._logger = logging.getLogger(name)
        f_handler = logging.FileHandler("log/{}.log".format(name))
        f_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_formatter)
        self._logger.addHandler(f_handler)
        self._logger.setLevel(logging.DEBUG)


    @property
    def logger(self):
        return self._logger

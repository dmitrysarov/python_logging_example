import logging
from logging import handlers

logger = logging.getLogger(__name__)
handler_stream = logging.StreamHandler() #output to console
logFile = 'ocr.log'
handler_file = handlers.RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024,
                                        backupCount=1, encoding=None, delay=0)
formatter = logging.Formatter("%(asctime)s:::%(module)s:::%(message)s")
handler_stream.setFormatter(formatter)
handler_file.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler_stream)
logger.addHandler(handler_file)
logger.info('hello world')

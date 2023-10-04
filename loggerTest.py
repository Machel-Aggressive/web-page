import logging
import time

logging.basicConfig(level=logging.NOTSET, filename='app.log', filemode='w', format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)
logger.debug('This is a debug message')
logger.info('This is an info message')
time.sleep(1)
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')



import logger


try:
    a = 1 / 0
except:
    logger.error("Something went wrong")

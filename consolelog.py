import os
from logging import getLogger, Formatter, StreamHandler, FileHandler, DEBUG, INFO, ERROR

LOG_DIR = "logs"
LOG_FILE = f"./{LOG_DIR}/program.log"

if not os.path.isdir(f"./{LOG_DIR}/"): os.mkdir(f"./{LOG_DIR}/")
def get_module_logger(module:str, verbose:bool):
    logger = getLogger(module)
    logger = _set_handler(logger, StreamHandler(), verbose)
    logger = _set_handler(logger, FileHandler(LOG_FILE), verbose)
    if verbose:
        logger.setLevel(DEBUG)
    else:
        logger.setLevel(INFO)
    logger.propagate = False
    return logger

def _set_handler(logger, handler, verbose):
    if verbose:
        handler.setLevel(DEBUG)
    else:
        handler.setLevel(INFO)
    handler.setFormatter(Formatter('%(name)s [%(levelname)s]: %(message)s'))
    logger.addHandler(handler)
    return logger
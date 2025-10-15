import logging
import sys
import os

def get_logger(name=__name__, log_file=None):
    logger = logging.getLogger(name)

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Handler for console
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # Handler for file if log_file is provided
    if log_file:
        file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)  # saving all logs
        logger.addHandler(file_handler)

    # logger's global level
    logger.setLevel(logging.DEBUG)

    return logger


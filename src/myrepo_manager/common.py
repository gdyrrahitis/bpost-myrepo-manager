import logging
import os

GIT_SERVER = os.getenv("GIT_SERVER")
GIT_SERVER_PORT = os.getenv("GIT_SERVER_PORT")


def get_logger(name):
    logger = logging.Logger(name or __name__, os.getenv("LOG_LEVEL") or 0)
    return logger

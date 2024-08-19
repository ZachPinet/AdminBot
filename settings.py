import os
import logging
from logging.config import dictConfig
from dotenv import load_dotenv

# Loads the dotenv file.
load_dotenv()

# Gets the private information stored in the dotenv file.
TOKEN = os.getenv('TOKEN')
TESTTOKEN = os.getenv('TESTTOKEN')
DBUSER =  os.getenv('DBUSER')
DBPASSWORD = os.getenv('DBPASSWORD')
CLUSTERSTRING = os.getenv('CLUSTERSTRING')
URI = f"mongodb+srv://{DBUSER}:{DBPASSWORD}@{CLUSTERSTRING}.mongodb.net/?retryWrites=true&w=majority"

# Configures the settings for the logs.
LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_Loggers": False,
    "formatters":{
        "verbose":{
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard":{
            "format": "%(levelname)-10s - %(name)-15s : %(message)s"
        },
    },
    "handlers":{
        "console": {
            'level': "DEBUG",
            'class': "logging.StreamHandler",
            'formatter': "standard"
        },
        "console2": {
            'level': "WARNING",
            'class': "logging.StreamHandler",
            'formatter': "standard"
        },
        "file": {
            'level': "INFO",
            'class': "logging.FileHandler",
            'filename': "logs/infos.log",
            'mode': "w",
            'formatter': "verbose"
        },
    },
    "Loggers":{
        "bot": {
            'handlers': ['console'],
            "level": "INFO",
            "propagate": False
        },
        "discord": {
            'handlers': ['console2', "file"],
            "level": "INFO",
            "propagate": False
        }
    }
}
# -*- coding: utf-8 -*-
"""
Main loggin modules
"""
__copyright__ = "Copyright (C) 2016 Veritas Technologies LLC. All rights reserved."

# std-lib imports
import os
import logging
from logging.config import dictConfig


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(levelname)s:%(name)s: (%(asctime)s; %(filename)s:%(lineno)d): '
                    '%(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        }
    },
    'handlers': {
        'user_console': {
            'level': 'INFO',
            'formatter': '',
            'class': 'logging.StreamHandler',
        },
        'console': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        # 'rotate_file': {
        #     'level': 'DEBUG',
        #     'formatter': 'standard',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': 'rotated.log',
        #     'encoding': 'utf8',
        #     'maxBytes': 100000,
        #     'backupCount': 1,
        # }
    },
    'loggers': {
        'dev': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'prod': {
            'handlers': ['user_console'],
            'level': 'INFO',
        },
    }
}
dictConfig(LOGGING)

# get the logger from sys environ variable
try:
    logger = os.environ['ARTIFACTORY_LOGGER']
    import requests
    requests.packages.urllib3.add_stderr_logger()
except:
    logger = "prod"

log = logging.getLogger(logger)
log.propagate = True

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = 'logs'
PROJECT_NAME = 'logsdemo'

LOG_FORMAT = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {module} | {function} | {message}"

LOG = {
    "handlers": [
        {
            "sink": sys.stdout,
            "format": LOG_FORMAT,
            "level": "DEBUG"
        },
        {
            "sink": os.path.join(BASE_DIR, LOGS_DIR, "%s_{time:YYYYMMDD}.log" % PROJECT_NAME),
            "serialize": False,  # True - convierte cada linea de log a JSON
            "format": LOG_FORMAT,
            "rotation": "1 days",
            "level": "DEBUG"
        },
    ],

}

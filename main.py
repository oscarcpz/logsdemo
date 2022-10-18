#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from random import randint
from time import sleep

from faker import Faker
from loguru import logger

from configurations.logger import LOG


def log(string, seconds):
    value = randint(0, 10)
    if value < 6:
        logger.debug(string)
    elif 5 < value < 8:
        logger.info(string)
    else:
        logger.error(string)
    sleep(seconds)  # sleep each 5 seconds


if __name__ == '__main__':
    logger.remove()  # remove default log
    logger.configure(**LOG)

    if len(sys.argv) != 3:
        logger.error('Wrong number of arguments')
        logger.info(f'Example: python {sys.argv[0]} 5 100000')
        logger.info('5 -> delay between log traces')
        logger.info('100000 -> number of log traces')
        sys.exit(-1)

    seconds = sys.argv[1]
    itr = sys.argv[2]

    if not seconds:
        logger.error('Seconds [first parameter is mandatory]')
        sys.exit(-1)

    if not seconds.isnumeric():
        logger.error('Seconds must be an integer')
        sys.exit(-1)

    if not itr:
        logger.error('Number of iterations is mandatory [second parameter]')
        sys.exit(-1)

    if not itr.isnumeric():
        logger.error('Number of iterations must be an integer')
        sys.exit(-1)

    fake = Faker()
    Faker.seed(0)

    # infinite loop!!!
    # kill this process with CTRL + c
    for _ in range(int(itr)):
        log(fake.sentence(nb_words=10), int(seconds))

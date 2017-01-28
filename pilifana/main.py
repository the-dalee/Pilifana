#!/usr/bin/env python3
from pilifana.core import run
from pilifana.config import ConfigWrapper
import os
import logging


def main(devmode=False):
    configfile = os.environ.get('PILIFANA_CONFIG_FILE')
    if not configfile:
        if devmode:
            configfile = "./configuration/config.yaml"
        else:
            configfile = "/etc/pilifana/config.yaml"
    config = ConfigWrapper(configfile)

    logformat = config.get('logging.format', 
                           default="%(asctime)s [%(levelname)s] |==> %(message)s", 
                           env='PILIFANA_LOGGING_FORMAT')

    loglevelconf = config.get('logging.level',
                              default="DEBUG",
                              env='PILIFANA_LOGGING_LEVEL')

    if loglevelconf == "DEBUG": loglevel = logging.DEBUG
    elif loglevelconf == "INFO": loglevel = logging.INFO
    elif loglevelconf == "WARNING": loglevel = logging.WARNING
    elif loglevelconf == "ERROR": loglevel = logging.ERROR
    elif loglevelconf == "CRITICAL": loglevel = logging.CRITICAL
    else: loglevel = logging.NOTSET  

    logging.basicConfig(format=logformat, level=loglevel)
    logging.info("Starting using config {0}".format(configfile))
    run(config)

if __name__ == '__main__':
    main(False)

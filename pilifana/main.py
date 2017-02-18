#!/usr/bin/env python3
import logging
import os

from pilifana.config import ConfigWrapper
from pilifana.conversion.loglevel import loglevel
from pilifana.core import run


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

    logging.basicConfig(format=logformat, level=loglevel(loglevelconf))
    logging.info("Using config {0}".format(configfile))
    run(config)

if __name__ == '__main__':
    main(False)

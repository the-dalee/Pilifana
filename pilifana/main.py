#!/usr/bin/env python3
import logging
import os
import sys
from daemonize import Daemonize

from pilifana.config import ConfigWrapper
from pilifana.conversion.loglevel import loglevel
from pilifana.core import run


def get_logger_config(config):
    format = config.get('logging.format',
                        default="%(asctime)s [%(levelname)s] |==> %(message)s",
                        env='PILIFANA_LOGGING_FORMAT')
    level = config.get('logging.level',
                       default="DEBUG",
                       env='PILIFANA_LOGGING_LEVEL')
    return format, loglevel(level)


def start_console(devmode=False):
    configfile = os.environ.get('PILIFANA_CONFIG_FILE')
    if not configfile:
        if devmode:
            configfile = "./configuration/config.yaml"
        else:
            configfile = "/etc/pilifana/config.yaml"
    config = ConfigWrapper(configfile)

    format, level = get_logger_config(config)

    logging.basicConfig(format=format, level=level)
    logging.info("Using config {0}".format(configfile))
    run(config)


def start_daemon():
    config = ConfigWrapper('/etc/pilifana/config.yaml')
    format, level = get_logger_config(config)
    pid = "/var/run/pilifana.pid"

    formatter = logging.Formatter(format)
    fh = logging.FileHandler("/var/log/pilifana.log", "w")
    fh.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(level)
    logger.addHandler(fh)

    keep_fds = [fh.stream.fileno()]

    def startdaemon():
        run(config=config)

    daemon = Daemonize(app="pilifana", pid=pid, action=startdaemon, keep_fds=keep_fds)
    daemon.start()


def main(devmode=False):
    if '--daemon' in sys.argv[1:]:
        start_daemon()
    else:
        start_console(devmode)

if __name__ == '__main__':
    main(False)

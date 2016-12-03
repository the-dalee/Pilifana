#!/usr/bin/env python3
from pilifana.core import run
from pilifana.config import ConfigWrapper
import os


def main(devmode=False):
    configfile = os.environ.get('PILIFANA_CONFIG_FILE')
    if not configfile:
        if devmode:
            configfile = "./configuration/config.yaml"
        else:
            configfile = "/etc/pilifana/config.yaml"
    config = ConfigWrapper(configfile)
    print("Starting using config {0}".format(configfile))
    run(config)

if __name__ == '__main__':
    main(False)

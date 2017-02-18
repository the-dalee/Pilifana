import logging
from daemonize import Daemonize

from pilifana.config import ConfigWrapper
from pilifana.conversion.loglevel import loglevel
from pilifana.core import run


def start():
    config = ConfigWrapper('/etc/pilifana/config.yaml')

    format = config.get('logging.format',
                         default="%(asctime)s [%(levelname)s] |==> %(message)s",
                         env='PILIFANA_LOGGING_FORMAT')

    level = config.get('logging.level',
                        default="DEBUG",
                        env='PILIFANA_LOGGING_LEVEL')

    pid = "/var/run/pilifana.pid"

    formatter = logging.Formatter(format)

    fh = logging.FileHandler("/var/log/pilifana.log", "w")

    fh.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(loglevel(level))
    logger.addHandler(fh)

    keep_fds = [fh.stream.fileno()]

    def startdaemon():
        run(config=config)

    daemon = Daemonize(app="pilifana", pid=pid, action=startdaemon, keep_fds=keep_fds)
    daemon.start()
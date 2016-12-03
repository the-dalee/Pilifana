from pilifana.conversion.structure import Flattener
from yaml import safe_load, YAMLError
import os


class ConfigWrapper:
    def __init__(self, filename):
        with open(filename, 'r') as stream:
            try:
                content = safe_load(stream)
                flattener = Flattener()
                self.config = flattener.flatten(content)
            except YAMLError as e:
                print(e)
                self.config = dict()
            except IOError as e:
                print(e)
                self.config = dict()

    def get(self, key, default=None, env=None):
        return os.getenv(env, self.config.get(key, default))

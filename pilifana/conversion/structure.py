class Flattener:
    def __init__(self, prefix=''):
        self.prefix = prefix

    def __flatten_list(self, structure, prefix):
        result = dict()

        for i, subitem in enumerate(structure):
            path = '{0}[{1}]'.format(prefix, i)
            flat = self.__flatten(subitem, path)

            for path, item in flat.items():
                result[path] = item

        return result

    def __flatten_dict(self, structure, prefix):
        result = dict()

        for subpath, subitem in structure.items():
            path = '{0}.{1}'.format(prefix, subpath) if prefix else subpath
            flat = self.__flatten(subitem, path)

            for path, item in flat.items():
                result[path] = item

        return result

    def __flatten_primitive(self, primitive, prefix):
        return {prefix: primitive}

    def __flatten(self, structure, prefix):
        result = dict()

        if type(structure) is dict:
            flat = self.__flatten_dict(structure, prefix)
        elif type(structure) is list or type(structure) is set:
            flat = self.__flatten_list(structure, prefix)
        else:
            flat = self.__flatten_primitive(structure, prefix)

        for path, item in flat.items():
            result[path] = item

        return result

    def flatten(self, structure):
        return self.__flatten(structure, self.prefix)
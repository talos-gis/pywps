from json import JSONEncoder


class ArrayEncoder(JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'tolist'):
            # this will work for array.array and numpy.ndarray
            return obj.tolist()
        return JSONEncoder.default(self, obj)

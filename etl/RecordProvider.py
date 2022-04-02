class RecordProvider:
    def __init__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __enter__(self):
        raise NotImplementedError()

    def __exit__(self, type, val, traceback):
        raise NotImplementedError()
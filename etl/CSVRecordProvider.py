import csv
from etl.RecordProvider import RecordProvider

class CSVRecordProvider(RecordProvider):
    def __init__(self, path):
        self.__path = path
        self.__setup = False

    def __enter__(self):
        self.__fd = open(self.__path, 'r')
        self.__setup = True
        return self
    
    def __iter__(self):
        if not self.__setup:
            raise RuntimeError("CSVRecordProvider must be used as context manager")
        
        self.__reader = csv.reader(self.__fd)
        return self.__reader.__iter__()

    def __next__(self):
        if not self.__setup:
            raise RuntimeError("CSVRecordProvider must be used as context manager")
        
        return self.__reader.__next__()

    def __exit__(self, type, val, traceback):
        self.__setup = False
        self.__fd.close()

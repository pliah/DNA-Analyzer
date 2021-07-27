from Batch.batch_pkg import List,Load ,Save,Show

from database import Database

class Batch:
    batch_name = ''
    __instance = None
    batch = False

    def __new__(cls, *args, **kwargs):
        if not Batch.__instance:
            Batch.__instance = object.__new__(cls)
        return Batch.__instance

    def __init__(self):
        self.__types = {
            "batchlist": List,
            "batchload": Load,
            "batchsave": Save,
            "batchshow": Show,

        }
        self.batch_database = Database()

    def executor(self, type, command):
        self.__types[type]().execute(command)

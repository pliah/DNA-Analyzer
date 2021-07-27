from Analysis.analysis import Analysis
from Batch.batch import Batch
from Create.create import Create
from Management.management import Management
from Manipulation.manipulation import Manipulation
from database import Database


class Command:

    def __init__(self):
        self.__types={
            "new": Create,
            "load": Create,
            "dup": Create,
            "pair": Manipulation,
            "replace": Manipulation,
            "del":Management,
            "save":Management,
            "find": Analysis,
            "findall": Analysis,
            "len":Analysis,
            "count":Analysis,
            "batch":Batch,
            "batchlist": Batch,
            "batchload": Batch,
            "batchsave": Batch,
            "batchshow": Batch,
            }
        self.database = Database()

    def handle_command(self,command):
        type = command[0]
        if type == "end":
            Batch.batch = False
        elif Batch.batch:
            self.database.add_to_batch_database(Batch.batch_name, command)
        else:
            command_exe = command[1:]
            self.__types[type.lower()]().executor(type,command_exe)


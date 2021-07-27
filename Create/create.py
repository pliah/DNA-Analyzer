from Create.create_pkg import New,Dup,Load
from database import Database



class Create:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Create.__instance:
            Create.__instance = object.__new__(cls)
        return Create.__instance

    def __init__(self):
        self.__types = {
            "new": New,
            "load": Load,
            "dup": Dup,
        }
        self.database = Database()


    def handle_command(self,command):
        for i in command:
            if i == '':
                command.remove(i)
        return command

    def is_valid_command(self,command):
        if len(command) == 0:
            return False
        else:
            return True
    def executor(self,type,command):
        command = self.handle_command(command)
        if self.is_valid_command(command):
            return_val = self.__types[type]().execute(command)
            self.database.add_to_database_dna(return_val)
            name = list(return_val.keys())[0]
            seq = str(return_val[name])
            if len(seq) > 41:
                seq = seq[1:32]+'...'+seq[-3:]
            print(f'[{self.database.counter}]  {name}: {seq}')
        else:
            raise Exception('You are missing arguments')


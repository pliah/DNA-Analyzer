from command import Command
from database import Database


class Run:

    def __init__(self):
        self.command = Command()

    def create_name(self, command_name):
        try:
             command_name[0]=command_name[0].replace('@', '')
             return ' '.join(command_name)
        except:
            raise IndexError("not a valid batch name to run")



    def execute(self,command):
        name = self.create_name(command)
        if name in list(Database.database_batch.keys()):
            for i in Database.database_batch[name]:
                if isinstance(i,str):
                    i =  i.split()
                self.command.handle_command(i)
        else:
            return ValueError("not a valid batch name")



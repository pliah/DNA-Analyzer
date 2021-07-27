from Analysis.analysis_pkg import Count,Find,FindAll,Len
from database import Database

class Analysis:
        __instance = None

        def __new__(cls, *args, **kwargs):
            if not Analysis.__instance:
                Analysis.__instance = object.__new__(cls)
            return Analysis.__instance

        def __init__(self):
            self.__types = {
                "findall":FindAll,
                "find": Find,
                "len": Len,
                "count": Count,
            }
            self.database = Database()

        def handle_command(self, command):
            for i in command:
                if i == '':
                    command.remove(i)
            return command

        def is_valid_command(self, command):
            if len(command) == 0:
                return False
            else:
                return True

        def find_seq_by_id_or_name(self, type, command):
            if command[0][0] == '#':
                id = command[1] if command[0] == '#' else command[0][1:]
                sequence = Database.get_sequence_by_id(id)
                name = Database.get_sequence_name_by_id(id)
                command = command[2:] if command[0] == '#' else command[1:]
            elif command[0][0] == '@':
                name = command[1] if command[0] == '@' else command[0][1:]
                sequence = Database.get_sequence_by_name(name)
                id = Database.get_sequence_id_by_name(name)
                command = command[2:] if command[0] == '@' else command[1:]
            if command != []:
                if  command[0][0] == '#':
                    id = command[1] if command[0] == '#' else command[0][1:]
                    command = Database.get_sequence_by_id(id)
                elif command[0][0] == '@':
                    name = command[1] if command[0] == '@' else command[0][1:]
                    command = Database.get_sequence_by_name(name)

            return sequence, name, command, id


        def executor(self, type, command):
            command = self.handle_command(command)
            if self.is_valid_command(command):
                seq_info = self.find_seq_by_id_or_name(type, command)
                self.__types[type]().execute(seq_info)
            else:
                raise Exception('You are missing arguments')
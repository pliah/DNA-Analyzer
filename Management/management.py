
from Management.manage_pkg import Delete,Save
from database import Database


class Management:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Management.__instance:
            Management.__instance = object.__new__(cls)
        return Management.__instance


    def __init__(self):
        self.__types = {
            "del": Delete,
            "save": Save,
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
            sub = command[2:] if command[0] == '#' else command[1:]
        elif command[0][0]  == '@':
            name = command[1] if command[0] == '@' else command[0][1:]
            sequence = Database.get_sequence_by_name(name)
            id = (Database.get_sequence_id_by_name(name)+1)
            command = command[2:] if command[0] == '@' else command[1:]
        return sequence, name , command , id



    def executor(self, type, command):
        command = self.handle_command(command)
        if self.is_valid_command(command):
            seq_info = self.find_seq_by_id_or_name(type, command)
            return_val = self.__types[type]().execute(seq_info)
            if type == 'del' and return_val:
                self.database.del_from_database_dna_by_id(seq_info[3])
                print(f"Deleted: [{int(seq_info[3])}] {seq_info[1]} : {seq_info[0]}")

        else:
            raise Exception('You are missing arguments')



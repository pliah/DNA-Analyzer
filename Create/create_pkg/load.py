from database import Database
from DnaSequence.dna_sequence import DnaSequence

class Load:
    def __init__(self):
        pass

    def execute(self, command):
        if len(command) == 0:
            raise IndexError('you should write a sequence in  the new command')
        file_name = self.is_exist_file_name(command)
        file = file_name[0]
        sequence_name = file_name[1]
        file_sequence = self.read_from_file(file)
        sequence = DnaSequence(file_sequence)
        if len(sequence_name) >= 1:
            if sequence_name[0][0] != '@':
                raise ValueError('not a valid command for load operator')
            else:
                sequence_name = self.create_name(sequence_name)
        if len(sequence_name) == 0:
            sequence_name = self.default_name(file)
        return {sequence_name: sequence}

    def default_name(self, name):
        return name[:-7] + '_' + str(Database.counter+1)

    def is_exist_file_name(self,command):
        file_path=''
        flag = False
        for i in command:
            if i.find('.rawdna'):
                file_path += i
                flag = True
                command_name = command[command.index(i)+1:]
                break
            else:
                file_path += i
        if not flag:
            raise FileNotFoundError('file is not valid')
        return (file_path, command_name)

    def read_from_file(self, file_name):
        with open(file_name) as f:
            sequence = ''.join(f.read().splitlines())
        return sequence


    def create_name(self, command_name):
        created_command = ''
        for i in command_name:
            created_command += '_' + i
        return created_command[2:]
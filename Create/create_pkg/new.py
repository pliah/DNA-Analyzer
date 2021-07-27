from database import Database
from DnaSequence.dna_sequence import DnaSequence

class New:

    def __init__(self):
        pass

    def execute(self,command):
        if len(command) == 0:
            raise IndexError('you should write a sequence in  the new command')
        sequence = DnaSequence(command[0])
        sequence_name=''
        if len(command) == 1:
            sequence_name = self.default_name()
        if len(command) > 1:
            if command[1][0] != '@':
                 raise ValueError('not a valid command for new operator')
            else:
               sequence_name = self.create_name(command[1:])
        if Database.is_name_exist(sequence_name):
            sequence_name = self.default_name()
        return {sequence_name: sequence}

    def default_name(self):
        return 'seq_' + str(Database.counter+1)

    def create_name(self,command_name):
        if len(command_name) == 1 and command_name[0] == '@':
            return self.default_name()
        created_command=''
        command_name[0]=command_name[0].replace('@','')
        for i in command_name:
            if i!='':created_command+=i+'_'
        return created_command[:-1]





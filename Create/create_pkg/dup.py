from database import Database
from DnaSequence.dna_sequence import DnaSequence

class Dup:

    def execute(self, command):

        if len(command) == 0:
            raise IndexError('you should write a sequence in  the new command')

        if command[0][0] == '#':
            sequence = Database.get_sequence_by_id(int(command[0][1:]))
            sequence_name = Database.get_sequence_name_by_id(int(command[0][1:])-1)
            counter = sequence.get_counter()
            sequence.set_counter(counter+1)

        elif len(command) == 1 or command[1] == '@':
            sequence_name =(command[0][1:].replace('@',''))
            sequence = Database.get_sequence_by_name(sequence_name)
            sequence.set_counter(sequence.get_counter() + 1)

        elif len(command) > 1:
            if command[1][0] != '@':
                raise ValueError('not a valid command for new operator')
            else:
                sequence_name = self.create_name(command[1:])
                sequence = Database.get_sequence_by_name(sequence_name)
                sequence.set_counter(sequence.get_counter() + 1)

        return {sequence_name+'_'+str(sequence.get_counter()): DnaSequence(str(sequence))}

    def create_name(self, command_name):
        command_name[0][0].replace('@', '')
        created_command = ''
        for i in command_name:
            created_command += '_' + i
        return created_command


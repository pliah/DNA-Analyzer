
from Manipulation.manipul_pkg import Pair,Replace
from database import Database
from DnaSequence.dna_sequence import DnaSequence


class Manipulation:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Manipulation.__instance:
            Manipulation.__instance = object.__new__(cls)
        return Manipulation.__instance


    def __init__(self):
        self.__types = {
            "pair": Pair,
            "replace": Replace,
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

    def malt_name_and_seq(self,type,command):
        if command[0][0] == '#':
            id = command[1] if command[0]=='#' else command[0][1:]
            sequence = Database.get_sequence_by_id(id)
            name = Database.get_sequence_name_by_id(id)
        elif command[0][0] == '@':
            name = command[1] if command[0] == '@' else command[0][1:]
            sequence = Database.get_sequence_by_name(name)
        if ':' in command:
            # create_pkg a new dna Data
            sequence = DnaSequence(sequence.get_string())
            if command[-1] == '@@':
                sequence.set_counter(sequence.get_counter() + 1)
                if type == "pair":
                    return sequence,name+'_p'+str(sequence.get_counter()),0
                if type == "replace":
                    return sequence, name + '_r' + str(sequence.get_counter()),0
            else:
                name = self.search_for_name(command)
            return (sequence, name , 0)
        else:
            # in place
            return (sequence, name, 1)


    def search_for_name(self,command):
        created_name=''
        for i in range(len(command)):
            if command[i] == ':':
                break
        for j in range(i+1,len(command)):
            if command[j][0] == '@':
                break
        command[j]=command[j].replace('@','')
        name = command [j+1:] if command[j] == '@' else command[j:]
        if not name:
            raise TypeError('not a valid command, you should insert a name after @')
        for k in name:
            if k != '': created_name += k + '_'
        return created_name[:-1]

    def command_action(self,command):
        created_command=[]
        for i in command:
            if i == ':':
                break
            if '@' not in i:
                created_command.append(i)
        return created_command

    def executor(self, type, command):
        command = self.handle_command(command)
        seq_info = self.malt_name_and_seq(type, command)
        command_action = self.command_action(command)
        if self.is_valid_command(command):
            return_val = self.__types[type]().execute(seq_info[0],command_action)
            seq_info[0].assign(return_val)
            if seq_info[2] == 0:
                self.database.add_to_database_dna({seq_info[1] : seq_info[0]})
            if len(return_val) > 41:
                return_val = return_val[1:32] + '...' + return_val[-3:]
            print(f'[{self.database.counter}]  {seq_info[1]}: {return_val}')
        else:
            raise Exception('You are missing arguments')



import os

from database import Database


class Save:

    def execute(self, command):
        file_name = self.is_exist_file_name(command)
        batch_name = self.search_for_name(command)
        if file_name == "":
           file_name = batch_name+'.dnabatch'
        self.write_to_file(file_name,batch_name)

    def write_to_file(self, file_name,batch_name):
        with open(file_name,'w+') as f:
            for i in Database.get_batch_info(batch_name):
                f.write(' '.join(i)+'\n')


    def search_for_name(self, command):
        created_name = ''
        for j in range(len(command)):
            if command[j][0] == '@':
                break
        command[j] = command[j].replace('@', '')
        name = command[j + 1:] if command[j] == '@' else command[j:]
        if not name:
            raise TypeError('not a valid command, you should insert a name of batch')
        for k in name[:-1]:
            if k != '': created_name += k + ' '
        return created_name[:-1]

    def is_exist_file_name(self,command):
        file_path = ''
        for i in command:
            if i.find('.')!= -1:
                file_path = i
                break
        return file_path
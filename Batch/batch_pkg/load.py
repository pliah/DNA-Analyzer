from database import Database


class Load:
    def __init__(self):
        self.database = Database()

    def execute(self, command):
        if len(command) == 0:
            raise IndexError('you should write a sequence in  the new command')

        file_name = self.is_exist_file_name(command)
        batch_name = self.search_for_name(command)
        if batch_name == '':
            index=file_name.find('.')
            batch_name = file_name[:index]
        while Database.is_batch_exist(batch_name):
             batch_name=input('your batch name is not available, please try another one\n')


        self.database.create_batch(batch_name)

        self.read_from_file(file_name,batch_name)

    def read_from_file(self, file_name,batch_name):
        with open(file_name) as f:
            lines = f.readlines()
            for line in lines:
                self.database.add_to_batch_database(batch_name,line[:-1])
        return


    def search_for_name(self, command):
        created_name = ''
        flag = False
        for j in range(len(command)):
            if command[j][0] == '@':
                flag = True
                break
        if flag:
            command[j] = command[j].replace('@', '')
            name = command[j + 1:] if command[j] == '@' else command[j:]
            if not name:
                raise TypeError('not a valid command, you should insert a name of batch')
            for k in name:
                if k != '': created_name += k + ' '
        return created_name[:-1]

    def is_exist_file_name(self,command):
        file_path = ''
        for i in command:
            if i.find('.')!= -1:
                file_path = i
                break
        return file_path
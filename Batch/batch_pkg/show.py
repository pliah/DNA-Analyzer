from database import Database

class Show:
    def execute(self, command):
        name = ' '.join(command)
        name=name.replace('@','')
        for i in Database.get_batch_info(name):
            print("   command: ", i)


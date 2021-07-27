from database import Database
class List:

    def execute(self,command):
        print("num of batches: ",len(Database.get_batches_names()))
        for i in Database.get_batches_names():
            print("   * batch: ", i)


# from Batch.batch import Batch


class Database:
    __instance = None
    database_dna = {}
    database_batch = {}
    counter = 0

    def __new__(cls, *args, **kwargs):
        if not Database.__instance:
            Database.__instance = object.__new__(cls)
        return Database.__instance

    @staticmethod
    def is_name_exist(name):
        if name  in list(Database.database_dna.keys()):
            return True
        return False

    @staticmethod
    def is_batch_exist(name):
        if name in Database.database_batch.keys():
            return True
        return False

    @staticmethod
    def get_sequence_by_name(name):
        if name not in list(Database.database_dna.keys()):
            raise KeyError('not such an dna name')
        return Database.database_dna[str(name)]

    @staticmethod
    def get_sequence_name_by_id(id):

        if len(list(Database.database_dna.keys())) < int(id):
            raise IndexError('no such a dna id')
        else:
            return list(Database.database_dna.keys())[int(id)-1]
    @staticmethod
    def get_sequence_id_by_name(name):
        if name not in list(Database.database_dna.keys()):
            raise IndexError('no such a dna id')
        else:
            return list(Database.database_dna.keys()).index(name)

    @staticmethod
    def get_sequence_by_id(id):
        if id == '':
            raise IndexError('lease put # before the id number')
        if len(list(Database.database_dna.values())) < int(id):
            raise IndexError('no such a dna id')
        else:
            return list(Database.database_dna.values())[int(id) - 1]

    def add_to_database_dna(self, val):
        Database.database_dna.update(val)
        Database.counter += 1


    def add_to_batch_database(self,batch_name,val):
        Database.database_batch[batch_name].append(val)



    def create_batch(self,name):
        Database.database_batch.update({name:[]})


    @staticmethod
    def get_batches_names():
        return Database.database_batch.keys()

    @staticmethod
    def get_batch_info(name):
        return Database.database_batch[name]

    def del_from_database_dna_by_id(self, id):
        if len(list(Database.database_dna.values())) < int(id):
            raise IndexError('no such a dna id')
        else:
            Database.database_dna.pop(list(Database.database_dna)[int(id)-1])
            Database.counter-=1


class Save:

    def execute(self, info):

        file = info[1]+'.rawdna'
        with open(file, "w+") as f:
            f.write(info[1]+' : ' + str(info[0]))
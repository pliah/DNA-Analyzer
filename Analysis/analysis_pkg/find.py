class Find:

    def execute(self, info):
        try:
            seq = str(info[0])
            sub = str(info[2][0])
            index = seq.index(sub)
            print(index+1)
        except:
            ValueError("string don't contain sub string")



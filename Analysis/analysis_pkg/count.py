class Count:
    def execute(self, info):
        index = 0
        i = 0
        seq = str(info[0])
        sub = str("".join(info[2]))
        try:
            while i < len(info[0]):
                if len(sub) > len(info[0]) - i:
                    break
                i = seq.index(sub)
                index+=1
                seq = seq[i + 1:]
                i += 1
            print(index)
        except:
            print(index)
            ValueError("string don't contain sub string")
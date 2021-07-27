class FindAll:
    def execute(self, info):
        index=[]
        i = 0
        prev = 0
        seq = str(info[0])
        sub = str("".join(info[2]))
        try:
            while i < len(info[0]):
                if len(sub)> len(info[0])-i:
                    break
                i = seq.index(sub)
                index.append(str(i+1 + prev))
                seq = seq[i+1:]
                prev += i+1
                i += 1
            print(' '.join(index))
        except:
            if index != []:
                print(' '.join(index))
            ValueError("string don't contain sub string")



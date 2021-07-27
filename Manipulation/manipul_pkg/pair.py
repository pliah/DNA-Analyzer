class Pair:
    def __init__(self):
        pass

    def execute(self,seq,comand_action):
        new_seq=''
        for i in seq:
            if i == 'T':
                new_seq += 'A'
            elif i == 'A':
                new_seq += 'T'
            elif i == 'C':
                new_seq += 'G'
            elif i == 'G':
                new_seq += 'C'
        return new_seq


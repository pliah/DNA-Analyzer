import re

class DnaSequence:

    def __init__(self,string):
        if not self.is_valid(string):
            raise TypeError('not a valid nucleotides')
        else:
            self._sequence = string
        self.__counter = 0

    # get string
    def get_string(self):
        return self._sequence

    def set_string(self,seq):
        self._sequence = seq

    def get_counter(self):
        return  self.__counter

    def set_counter(self,counter):
        self.__counter = counter

    def insert(self,nucleotide_val,index):
        if index>=len(self._sequence):
            raise IndexError
        if self.is_valid(nucleotide_val):
          self._sequence= self._sequence[:index] + nucleotide_val + self._sequence[index:]
        else:
            raise TypeError('not a valid nucleotides')

    def is_valid(self,string):
        valid = re.compile('[^A,G,C,T]')
        if valid.findall(string):
            return False
        return True
    # def __assign__(self, other):
    #     if isinstance(other,str):
    #         other = DnaSequence(other)
    #         self=other
    #     if isinstance(other, self):
    #         self.__string = other.get_string()
    #     return self

    def assign(self, other):

        if isinstance(other,str):
            if self.is_valid(other):
               self._sequence=other
            else:
                raise TypeError('not a valid nucleotides')
        if isinstance(other,DnaSequence):
            other_str=other.get_string()
            if self.is_valid(other_str):
                self._sequence = other_str
            else:
                raise TypeError('not a valid nucleotides')
        else:
            ValueError('not a valid type to assign')
        return self

    def __str__(self):
        return "{}".format(self._sequence)

    def __rpr__(self):
        return "{}".format(self._sequence)

    def __eq__(self, other):
        return other.get_string() == self._sequence

    def	__ne__(self, other):
        return not other.get_string() == self._sequence

    def __setitem__(self, key,val):
        if int(key)>=len(self._sequence):
            raise IndexError
        if self.is_valid(val):
            self._sequence= self._sequence[:key] + val + self._sequence[key + 1:]
        else:
            raise TypeError('not a valid nucleotides')

    def __getitem__(self, key):
        if key >= len(self._sequence):
            raise IndexError
        return self._sequence[key]

    def __len__(self):
        return len(self._sequence)

# dna=DnaSequence("ACT")
# print(dna.get_string())
# dna.insert(23,1)
# print(dna.get_string())
# # print(isinstance("dna",str))
# # other = "xdfg"
# other = DnaSequence("aba")
# dna=other
# dna.assign(3)
# print(dna.get_string())
# print(dna!=other)
# print(dna[0])
# print(len(dna))
# print(dna[0])
# dna[0]='A'
# print(dna[0])
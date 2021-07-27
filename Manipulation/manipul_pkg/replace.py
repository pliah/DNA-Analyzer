class Replace:


    def execute(self, seq, command_action):
        valid_dna=['T','A','C','G']
        for i in range(0, len(command_action), 2):
            if i ==len(command_action)-1 or i>=len(seq):
                raise IndexError("not such an index")
            if command_action[i + 1] in valid_dna:
                if not isinstance(int(command_action[i]), int):
                    raise ValueError('not a valid index')
                seq[int(command_action[i])] = command_action[i + 1]
        return seq
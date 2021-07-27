

class Delete:

    def execute(self, info):
        valid =['y','n']
        print(f"Do you really want to delete {info[1]} : {info[0]}? \n"
              f"Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.")
        confirm = input("> confirm >> > ")

        while confirm.lower() not in valid:

            print("You have typed an invalid response.\nPlease either confirm by 'y' / 'Y', or cancel by 'n' / 'N'.")
            confirm = input("> confirm >> > ")
        if confirm.lower() == 'y':
            return True
        return False

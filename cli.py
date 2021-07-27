from Batch.batch import Batch
from Batch.batch_pkg.run import Run
from command import Command
from database import Database


class CLI:
    def __init__(self):
        self._command = Command()
        self.batch_database = Database()


    def del_spaces(self, command):
        command = " ".join(command.split())
        new_command = command.split(' ')
        " ".join(new_command)
        return new_command

    def run(self):
        while True:
            # try:
                if not Batch.batch:
                    new_command = input('> cmd >>> ')
                else:
                    new_command = input('> batch >>> ')

                command = self.del_spaces(new_command)

                if command[0] == "batch" and not Batch.batch:
                    Batch.batch = True
                    Batch.batch_name = ' '.join(command[1:])
                    if Database.is_batch_exist(Batch.batch_name):
                        print('your batch name is not available, please try another one')
                        Batch.batch = False
                    self.batch_database.create_batch(Batch.batch_name)
                elif command[0].lower() == 'run':
                    Run().execute(command[1:])
                else:
                    self._command.handle_command(command)
            #
            # except KeyError:
            #     print('not a valid command')
            # except ValueError as ve:
            #     print(ve.args)
            # except TypeError as te:
            #     print(te.args)
            # except IndexError as ie:
            #     print(ie.args)
            # except FileNotFoundError as f:
            #     print(f.args)
            # except Exception as e:
            #     print(e.args)


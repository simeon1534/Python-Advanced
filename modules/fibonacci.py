# fibonacci/executor.py

from . import create_sequence


class Executor:
    def __init__(self):
        self.__sequence = []

    def run(self):
        while True:
            res = self.run_once()
            if not res:
                break

    def run_once(self):
        command = input()
        if command.startswith('Create Sequence '):
            return self.__handle_create(command)
        elif command.startswith('Locate '):
            return self.__handle_locate(command)
        elif command == 'Stop':
            return self.__handle_stop(command)
        return True

    def __handle_create(self, command):
        n = int(command.split()[-1])
        self.__sequence = create_sequence(n)
        print(self.__sequence)
        return True

    def __handle_locate(self, command):
        search = int(command.split()[-1])
        try:
            pos = self.__sequence.index(search)
            print(f'The number - {search} is at index {pos}')
        except ValueError:
            print(f'The number {search} is not in the sequence')
        except NameError:
            print('Make sure to create sequence first')
        return True

    def __handle_stop(self, command):
        return False


# fibonacci/__init__.py
def create_sequence(n):
    assert n >= 1
    if n == 1:
        sequence = [0]
    elif n == 2:
        sequence = [0, 1]
    else:
        sequence = [0, 1]
        for _ in range(0, n - 2):
            sequence.append(sequence[-1] + sequence[-2])
    return sequence


# 05-fib.py
from fibonacci.executor import Executor

executor = Executor()
executor.run()
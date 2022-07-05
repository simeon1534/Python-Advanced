import os

path='my_first_file.txt'
try:
    os.remove('C:\\GOG Games/file_test.txt')
except FileNotFoundError:
    print('File already deleted!')

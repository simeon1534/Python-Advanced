import os

data = input()
while not data == "End":
    processed_data = data.split('-')
    if processed_data[0] == 'Create':
        command, file_name = processed_data
        file = open(f'{file_name}', 'w')
        file.close()
    elif processed_data[0] == 'Add':
        command, file_name, content_to_add = processed_data
        with open(f'{file_name}', 'a') as file_adding:
            print(f"{content_to_add}", file=file_adding)
    elif processed_data[0] == 'Replace':
        command, file_name, old_string, new_string = processed_data
        try:
            fin = open(f"{file_name}", 'r' )
            # read file contents to string
            data = fin.read()
            # replace all occurrences of the required string
            data = data.replace(old_string, new_string)
            # close the input file
            fin.close()
            # open the input file in write mode
            fin = open(f"{file_name}", 'w' )
            # overrite the input file with the resulting data
            fin.write(data)
            # close the file
            fin.close()

        except FileNotFoundError:
            print("An error occurred")
    elif processed_data[0] == 'Delete':
        command, file_name = processed_data
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

    data = input()

import os

directory = 'C:\\Users/Simeon/PycharmProjects/file_handling_exercises'
files_list = []
extensions = set()
for file in os.listdir(directory):
    f = os.path.join(directory, file)
    # checking if it is a file
    if os.path.isfile(f):
        file_name, file_extension = file.split('.')
        files_list.append(tuple(file.split('.')))
        extensions.add(file_extension)

sorted_list = sorted(files_list, key=lambda a: a[1])
extensions = sorted(list(extensions))

print(extensions)
print(files_list)
print(sorted_list)

report_fh_w = open('report.txt', 'w')
report_fh_w.close()

for ext in extensions:
    with open('report.txt', 'a') as report_fh_w:
        print(f'.{ext}', file=report_fh_w)
        for tupl_files in sorted_list:
            name, file_ext = tupl_files
            if file_ext == ext:
                print(f"- - - {name}.{file_ext}", file=report_fh_w)

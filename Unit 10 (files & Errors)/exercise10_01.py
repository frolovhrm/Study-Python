
file_name = 'learning_python.txt'

with open(file_name) as file_object:
    line = file_object.readlines()


for line in line:
    print(line)

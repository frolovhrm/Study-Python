file_name = 'learning_python.txt'

with open(file_name) as file_object:
    line = file_object.readlines()

with open(file_name) as file_object:
    line2 = file_object.read()


for line in line:
    print(line.replace('Python', 'C#').strip())

print('')

print(line2.replace('Python', 'Java'))

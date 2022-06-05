file_name_1 = 'cats.txt'
file_name_2 = 'dogs.txt'

try:
    with open(file_name_1, encoding='utf-8') as f:
        print(f.read() + '\n')

except FileNotFoundError:
    print()

try:

    with open(file_name_2, encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('Файл не найден')

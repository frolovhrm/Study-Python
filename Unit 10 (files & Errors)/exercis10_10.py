file_name_1 = 'A Little Princess.txt'
file_name_2 = 'The Pink Fairy Book.txt'

with open(file_name_1, encoding='utf-8') as f:
    my_text = f.read()
    print(my_text.lower().count('the '))

with open(file_name_2, encoding='utf-8') as k:
    my_text = k.read()
    print(my_text.lower().count('the '))

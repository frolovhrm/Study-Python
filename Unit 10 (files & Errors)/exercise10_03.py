user_name = input('Введите имя: ')
with open('guest.txt', 'w') as file_object:
    file_object.write(user_name + '\n')
    file_object.write('Sonia')

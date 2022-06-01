file_name = 'Guest_book.txt'

with open(file_name, 'w') as file_object:
    while True:
        input_name = input("Inter your name, please (inter 'q' to quite): ")
        if input_name == 'q':
            break
        file_object.write(input_name + '\n')

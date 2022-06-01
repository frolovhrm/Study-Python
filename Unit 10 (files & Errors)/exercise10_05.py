file_reasons = 'reasons.txt'
count = 1

with open(file_reasons, 'w') as file_object:
    while True:
        answer = input('Why are you like Python? (inter "q" to quite): ')
        if answer == 'q':
            break
        file_object.write(str(count) + '. ' + answer + '\n')
        count += 1

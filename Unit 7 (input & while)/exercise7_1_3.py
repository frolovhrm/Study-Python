"""Упражнение 7.1"""

message = input('What car do you want to get: ')
print(f'Let me see if I can find you a {message}')

"""Упражнение 7.2"""

quest = input('How many person, will be stay: ')
quest = int(quest)

if quest > 8:
    print('Sorry You have to wait')
else:
    print('Your table is ready')

"""Упражнение 7.3"""

num = input('Input your number: ')

if int(num) % 10 == 0:
    print('Число кратное 10!')
else:
    print('Число не кратное 10')

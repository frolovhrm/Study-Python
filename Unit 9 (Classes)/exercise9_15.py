import random

over_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']
win_ticket = []
my_ticket = ['8', '9', 'A', 'B']
count = 1


while True:
    win_ticket = random.sample(over_list, 4)
    if my_ticket == win_ticket:
        print(f'Попытка {count}, мой билет выиграл {my_ticket} = {win_ticket}')
        break
    count += 1





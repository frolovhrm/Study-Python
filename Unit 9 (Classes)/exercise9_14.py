import random

over_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']
win_ticket = []

while len(win_ticket) != 4:
    win_ticket.append(random.choice(over_list))

print(f'Выиграл билет номер: {win_ticket}')


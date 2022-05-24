"""Упражнение 7.4"""

# while True:
#     topping = input("what topping would you want to add: ")
#     if topping == 'quit':
#         break
#     else:
#         print('topping is added')

"""Упражнение 7.5"""

active = True
while active:
    age = input('how old are you? : ')
    age = int(age)
    if age < 3: print('Your ticket is free')
    if age < 12: print('Your ticket cost is 10$')
    if age > 135:
        print('Peaple do not life so long')
        active = False
    else: print('Your ticket cost is 15$')

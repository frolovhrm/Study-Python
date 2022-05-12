# names = ['Ivan', 'Oleg', 'Grisha', 'Alex', 'Admin']
#
# # names = []
#
# if len(names) == 0: print('We need to ind some users!')
#
# for names in names:
#
#     if names == 'Admin':
#         print('Hellow', names, ', would you like to see a status report?')
#     else:
#         print('Hellow', names, ', thank you for logging in again')

current_users = ['Ivan', 'Oleg', 'Grisha', 'Alex', 'Admin']

current_users_small= []

for current_users in current_users:
    current_users_small.append(current_users.lower())

print(current_users_small)

new_users = ['Olga', 'OLEG', 'Elly', 'Fox', 'Admin']

for new_users in new_users:
    if new_users.lower() in current_users_small:
        print('The name', new_users,'was used, please input new name')
    else: print(new_users, 'is a good name')
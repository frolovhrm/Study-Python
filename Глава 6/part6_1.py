man = {'fist_name': 'Ivan', 'last_name': 'Ivanov', 'age': 33, 'city': 'Moscow'}
lang = {'Ivan': 'C', 'Olga': 'Ruby', 'Eva': 'Go', 'Alexey': 'Python'}

# print(f"fist_name - {man['fist_name']}")
# print(f"last_name - {man['last_name']}")
# print(f"age - {man['age']}")
# print(f"city - {man['city']}")
# print('\n')
#
# print(f"fist_name - {man['fist_name']} \nlast_name - {man['last_name']} \nage - {man['age']} \ncity - {man['city']}")
#
# for k, v in man.items():
#     print(f'{k} - {v}')

friends = ['Ivan', 'Olga']

for name in lang.keys():
    print(name)

    if name in friends:
        # l = lang[name]
        print(f'{name} I know you, you study {lang[name]} \n')


import json

file_name = 'fnumber.json'
favorite_num = input('Введите ваше любимое число: ')

with open(file_name, 'w') as f:
    json.dump(favorite_num, f)

with open(file_name) as f:
    fnumber = json.load(f)

print(fnumber)

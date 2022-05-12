name = ['anton', 'egor', 'oleg']

name[0] = 'kent'

for i in name:
    print('Уважаемый ' + i.title() + ' приглашаем вас на ... ')

name.append('djuk')

print(name)

name.insert(1, 'shurik')

print(name)

del name[0]

print(name)

poped_name = name.pop()

print(poped_name)
print(name)

print(f'Крайний кекс это {poped_name.title()}.')

name.remove('oleg')
name.insert(-1, 'igor')
name.append('Igor2')

print(name)
print(name.count('igor'))
name.sort()

print(name)
name.sort(reverse=True)
print(name)

name.reverse()
print(name)
print(len(name))
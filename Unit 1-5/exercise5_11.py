# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = []

for i in range(1, 10):
    numbers.append(i)

for numbers in numbers:
    if numbers == 1:
        print('1st')
    elif numbers == 2:
        print('2nd')
    elif numbers == 3:
        print('3rd')
    else:
        print(f'{numbers}th')

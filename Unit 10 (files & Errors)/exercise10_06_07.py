while True:
    num_1 = input("Введите первое число ('q' выход): ")
    if num_1 == 'q':
        break
    num_2 = input('Введите второе чисор: ')

    sum_ex = 0

    try:
        sum_ex = int(num_1) + int(num_2)
        print(f'Сумма двух чисел = {sum_ex}\n')
    except ValueError:
        print('Вы ввели не число\n')

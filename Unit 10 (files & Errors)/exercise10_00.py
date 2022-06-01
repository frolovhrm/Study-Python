# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(f'{contents.rstrip()}\n******')
#
# filename = 'pi_digits.txt'
#
# with open(filename) as file_object:
#     for line in file_object:
#         print(f'{line.rstrip()}\n*****')
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# print(lines)
#
# with open(filename) as file_object:
#     contents = file_object.read()
#     print(f'{contents.rstrip()}\n*****')
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(f'{pi_string}\n')
# print(f'{len(pi_string)}\n*****')
#
# ex = float(pi_string.strip())
# print(f'{type(ex)}\n*****')
# print(f'{ex}\n*****')

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

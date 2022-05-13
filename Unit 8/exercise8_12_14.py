"""Упражнение 12"""

# def make_sandwich(*args):
#     print('\nSandwich make:')
#     for args in args:
#         print(f'- {args}')
#
#
# make_sandwich('bread', 'salad', 'cheese', 'onion')
#
# make_sandwich('bread', 'cheese', 'tomato')
#
# make_sandwich('bread', 'paprika')

"""Упражнение 13"""


# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
#
# user_profile = build_profile('Alexey', 'Frolov', location='Moscow', field='IT')
#
# print(user_profile)

"""Упражнение 14"""

def make_car(brend, model, **car):
    car['brend'] = brend
    car['model'] = model
    return  car

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
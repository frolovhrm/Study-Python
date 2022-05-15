"""Упражнение 1"""

# class Restaurant():
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         full_name = f'{self.restaurant_name}, {self.cuisine_type}'
#         return full_name
#
#     def open_restaurant(self):
#         print(f'\nThe restaurant {self.describe_restaurant()} food is open!')
#
#
# first_restaurant = Restaurant('Willy', 'Italian')
# second_restaurant = Restaurant('May', 'Russian')
# third_restaurant = Restaurant('Dog', 'American')
#
# Restaurant.open_restaurant(first_restaurant)
# Restaurant.open_restaurant(second_restaurant)
# Restaurant.open_restaurant(third_restaurant)

"""Упражненеи 3"""


class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} - {self.age}')

    def greet_user(self):
        print(f'I realy cute to see you {self.first_name} {self.last_name}')


one = User('Ivan', 'Ivanov', 22)
two = User('Sergey', 'Popov', 44)
three = User('Irina', 'Sokol', 18)

User.describe_user(one)
User.greet_user(one)

User.describe_user(two)
User.greet_user(two)

User.describe_user(three)
User.greet_user(three)

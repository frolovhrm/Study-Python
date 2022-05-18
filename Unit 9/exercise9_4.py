""" Упражнение 4 """

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        full_name = f'{self.restaurant_name}, {self.cuisine_type}'
        return full_name

    def open_restaurant(self):
        print(f'\nThe restaurant {self.describe_restaurant()} food is open, clients - {self.number_served} !')

    def set_number_served(self):
        number_served_input = int(input('Inter client served over: '))
        self.number_served = number_served_input

    def increment_number_served(self):
        self.number_served += 20



first_restaurant = Restaurant('Willy', 'Italian')


Restaurant.set_number_served(first_restaurant)

Restaurant.increment_number_served(first_restaurant)

Restaurant.open_restaurant(first_restaurant)

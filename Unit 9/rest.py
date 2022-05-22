class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def print_rest(self):
        print(f'name: {self.restaurant_name}\ncuisine: {self.cuisine_type}')



class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def print_rest(self):
        print(f'name: {one.restaurant_name}\ncuisine: {one.cuisine_type}\nflavors: {one.flavors}')


one = IceCreamStand('Funtik', 'IceCream', ('vanilla', 'cream'))

IceCreamStand.print_rest(one)


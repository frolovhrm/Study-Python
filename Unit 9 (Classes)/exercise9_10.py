from class_restaurant import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors=''):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def print_rest(self):
        print(f'name: {self.restaurant_name}\ncuisine: {self.cuisine_type}\nflavors: {self.flavors}')


one = IceCreamStand('Funtik', 'IceCream', ['vanilla', 'cream'])

two = Restaurant('Name', 'Type')

one.print_rest()
two.print_rest()
print()
IceCreamStand.print_rest(one)
Restaurant.print_rest(two)

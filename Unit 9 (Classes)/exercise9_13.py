import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides


    def roll_die(self):
        print(f'\nГраней у кубика {self.sides}:')
        shot = 1
        while shot < 11:
            random_sides = random.randrange(1, int(self.sides) + 1)
            print(f'\tбросок {shot} результат\t- {random_sides}')
            shot += 1


def roll_die(sides):
    print(f'\nГраней у кубика {sides}:')
    shot = 1
    while shot < 11:
        random_sides = random.randrange(1, int(sides) + 1)
        print(f'\tбросок {shot} результат\t- {random_sides}')
        shot += 1


cube = Die()
cube.roll_die()

cube = Die(10)
cube.roll_die()

cube = Die(20)
roll_die(cube.sides)

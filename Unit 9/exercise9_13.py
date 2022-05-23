import random


class Die:
    def __init__(self, sides):
        self.sides = sides


def roll_die(sides):
    print(f'\nГраней у кубика: {sides}')
    shot = 1
    while shot < 11:
        random_sides = random.randrange(1, int(sides) + 1)
        print(f'\tбросок {shot} результат\t- {random_sides}')
        shot += 1


cube = Die(6)
roll_die(cube.sides)

cube2 = Die(10)
roll_die(cube2.sides)

cube3 = Die(20)
roll_die(cube3.sides)

class Employee:

    def __init__(self, firstname, lastname, full_salary):
        self.firstname = firstname
        self.lastname = lastname
        self.full_salary = full_salary

    def give_raise(self, new_raise=0):

        if new_raise:
            return self.full_salary + new_raise
        else:
            return self.full_salary + 5000


first = Employee('Ivan', 'Ivanov', 5000)

print(first.give_raise())
print(first.give_raise(5001))

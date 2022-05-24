class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} - {self.age}')

    def greet_user(self):
        print(f'I really cute to see you {self.first_name} {self.last_name}')


class Admin(User):
    def __init__(self, first_name, last_name, age, privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = privileges

    def show_privileges(self):
        print(two.privileges)

    def greet_user(self):
        print(f'{self.first_name} {self.last_name} is admin')


one = User('Ivan', 'Ivanov', 22)

two = Admin('Petrov', 'Petr', 33, ['разрешено добавлять сообщения'])

User.describe_user(one)
User.greet_user(one)

Admin.describe_user(two)
Admin.greet_user(two)
Admin.show_privileges(two)

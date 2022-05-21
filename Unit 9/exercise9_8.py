class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} - {self.age}')

    def greet_user(self):
        print(f'I really cute to see you {self.first_name} {self.last_name}')


class Privileges():
    def __init__(self, privileges=['разрешено добавлять сообщения']):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name, age, ):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()

    def greet_user(self):
        print(f'{self.first_name} {self.last_name} is admin')


three = Admin('Alex', 'Lee', 44)

Admin.greet_user(three)
three.privileges.show_privileges()

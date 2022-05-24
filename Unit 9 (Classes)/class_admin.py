from class_user import User

class Privileges:
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
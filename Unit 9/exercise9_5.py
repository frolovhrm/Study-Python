class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} - {self.age} user number {self.login_attempts}')

    def greet_user(self):
        print(f'I really cute to see you {self.first_name} {self.last_name}')


one = User('Ivan', 'Ivanov', 22)

while True:
    User.increment_login_attempts(one)
    User.describe_user(one)
    if one.login_attempts > 3:
        User.reset_login_attempts(one)
        print('')
        break

User.describe_user(one)

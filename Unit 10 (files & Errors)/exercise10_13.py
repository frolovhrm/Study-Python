import json


def get_name():
    username = input('What is your name? :')
    filename = 'user_name.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")


def greet_user():
    """Приветствует пользователя по имени"""
    username = get_stored_username()

    if username:
        q = input(f'Is this your name {username} (y/n)? :')
        if q == 'y':
            print(f'Welcome beck, {username}!')
        if q == 'n':
            get_name()

    else:
        get_name()


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'user_name.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


greet_user()

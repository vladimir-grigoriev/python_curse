users = {
    'user1': 'pass1',
    'user2': 'pass2',
    'user3': 'pass3'
}


def decorator(func):
    def wrapper(*args, **kwargs):
        login = input('Enter login: ')
        password = input('Enter password: ')
        if login not in users.keys() or users[login] != password:
            return 'Autorization required'
        a = func(*args, **kwargs)
        return a

    return wrapper


@decorator
def sum_numbers(a, b):
    return a+b


print(sum_numbers(2, 3))

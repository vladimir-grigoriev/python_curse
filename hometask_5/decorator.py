creds = {'name1': 'pass1',
         'name2': 'pass2',
         }


def auth_required(func):
    def wrapper(*args, **kwargs):
        login = input('Введите ваш логин: ')
        password = input('Введите пароль: ')
        if login in creds.keys():
            if creds[login] == password:
                pass
            else:
                return 'Неверный пароль!'
        else:
            return 'Такого пользователя не существует!'
        value = func(*args, **kwargs)
        return value
    return wrapper


@auth_required
def some_func():
    return ('Добро пожаловать в систему!')


print(some_func())

from controllers import command_dict
from views import greetings


def main():
    while True:
        print(greetings)
        user_command = input('Введите команду: ')
        command_dict.get(user_command)()

    

if __name__ == "__main__":
    main()
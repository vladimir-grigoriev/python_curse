# Прописываем бизнес-логику
from models import User, PhoneNumbers
from models import session
import os

def show_user_list_controller():  # Выводим список пользователей
    os.system('clear||cls')
    users = session.query(User)
    for user in users:
        print('Пользователь -', user.name)
        print('Номера телефонов:')
        for number in user.phone:
            print(number.phone_number)
        print('=================')
    input()
    os.system('clear||cls')



def add_new_user_controller():  # Добавляем нового пользователя
    os.system('clear||cls')
    adding_user = User(name=input('Введите имя нового пользователя: '))
    session.add(adding_user)
    session.commit()
    adding_phone = PhoneNumbers(phone_number=input('Введите номер телефона: '), user_id=adding_user.id)
    session.add(adding_phone)
    session.commit()
    os.system('clear||cls')
    


def update_user_controller():  # Изменяем данные пользователя
    os.system('clear||cls')
    print('1. Изменить имя\n' + \
          '2. Добавить номер телефона\n' + \
          '0. Выйти в главное меню')
    command = input('')
    if command == '1':
        os.system('clear||cls')
        users = session.query(User)
        for user in users:
            print(user.id, user.name)
        changing = session.query(User).filter(User.id == input('Выберите пользователя: ')).first()
        changing.name = input('Введите новое имя: ')
        os.system('clear||cls')
    elif command == '2':
        os.system('clear||cls')
        users = session.query(User)
        for user in users:
            print(user.id, user.name)
        changing = session.query(PhoneNumbers).filter(PhoneNumbers.id == input('Выберите пользователя: ')).first()
        new_phone = PhoneNumbers(phone_number=input('Введите номер телефона: '), user_id=changing.user_id)
        session.add(new_phone)
        session.commit()
    else:
        os.system('clear||cls')



def delete_user_controller():  # Удаляем пользователя
    os.system('clear||cls')
    users = session.query(User)
    for user in users:
        print(user.id, user.name)
    deleting = session.query(User).filter(User.id == input('Выберите пользователя: ')).first()
    session.delete(deleting)
    session.commit()
    os.system('clear||cls')


def exit_program_controller():  # Выход из программы
    os.system('clear||cls')
    print('Программа завершена!')
    exit()


command_dict = {
    '1': show_user_list_controller,
    '2': add_new_user_controller,
    '3': update_user_controller,
    '4': delete_user_controller,  
    '0': exit_program_controller,
}
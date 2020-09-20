class Person():  # Пользователь калькулятора
    '''
    Класс пользователя калькулятора.
    Включает в себя его параметры (имя, рост, вес, возраст и пол),
    а также производит расчет индекса массы тела и позволяет
    изменять/добавлять пользователей
    '''
    def __init__(self, name, height, weight, age, sex):  # Инициализация
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex

    def bmi_calc(self):  # Расчет индекса массы тела
        return round(self.weight / (self.height**2), 2)

    def get_atributes(self):  # Возвращает данные пользователя
        answer = 'Пользователь ' + self.name + ', ' + str(self.age) + ' лет\n'\
                 'пол: ' + str(self.sex)+'\n'\
                 'рост: ' + str(self.height) + ' м\n'\
                 'вес: ' + str(self.weight) + ' кг\n'\
                 'индекс массы тела: ' + str(self.bmi_calc()) + ' кг/м2'
        return answer

    def scale(self):  # Возвращает рекомендации пользователю по его параметрам
        i = self.bmi_calc()
        return '\n\n############## Шкала ##############\n\n'+str(SCALE_START)\
            + '*' * (int(round(i, 0)) - SCALE_START - 1) + '||' + '*' *\
            (SCALE_END - int(round(i, 0)) - 1) + str(SCALE_END) + '\n\n'

    def recommendations(self):  # Рекомендации исходя из введенных данных
        if self.sex == 'male':
            if self.bmi_calc() < 18.5:
                if self.age < 30:
                    return 'Парень, тебе ' + str(self.age) + ' лет, а индекс ' + \
                           'массы тела всего ' + str(self.bmi_calc()) + ', стара' + \
                           'йся больше питаться и увеличь силовую нагрузку'
                else:
                    return 'Мужчина, вам ' + str(self.age) + ' лет, а индекс ' + \
                           'массы тела всего ' + str(self.bmi_calc()) + ', как-то ' + \
                           'несолидно для такого возраста. ' + \
                           'Больше питайтесь и займитесь спортом'
            elif self.bmi_calc() > 25:
                if self.age < 30:
                    return 'Парень, тебе ' + str(self.age) + ' лет, а индекс ' + \
                           'массы тела целых ' + str(self.bmi_calc()) + ', давай-ка ' + \
                           'садись на диету и займись спортом!'
                else:
                    return 'Мужчина, вам ' + str(self.age) + ' лет, а индекс ' + \
                           'массы тела целых ' + str(self.bmi_calc()) + ', пора бы ' + \
                           'уже поменьше уделять времени пиву и рыбалке ' + \
                           'и заняться спортом'
            else:
                return 'У вас все хорошо, не занимайте голову этой ерундой =)'
        elif self.sex == 'female':
            if self.bmi_calc() < 18.5:
                if self.age < 30:
                    return 'Девушка, вам ' + str(self.age) + ' лет, а индекс ' + \
                           'массы тела всего ' + str(self.bmi_calc()) + ', ' + \
                           'советую вернуться жить к маме, пока показатель ' + \
                           'не нормализуется'
                else:
                    return 'Мадам, вам ' + str(self.age) + ' лет, а индекс ' + \
                           'массы тела всего ' + str(self.bmi_calc()) + ', ' + \
                           'старайтесь больше питаться и займитесь спортом!'
            elif self.bmi_calc() > 25:
                if self.age < 30:
                    return 'Девушка, вам ' + str(self.age) + ' лет, а индекс ' + \
                           'массы тела целых ' + str(self.bmi_calc()) + ', ' + \
                           'давайте-ка садитесь на диету и займитесь спортом!'
                else:
                    return 'Мадам, вам ' + str(self.age) + ' лет, а индекс ' + \
                           'массы тела целых ' + str(self.bmi_calc()) + ', ' + \
                           'покупайте домик в деревне и заведите кроликов'
            else:
                return 'У вас все хорошо, не занимайте голову этой ерундой =)'
        else:
            return '\n' + self.sex.capitalize() + ' является ' + \
                'неподдерживаемым полом, сорян =(\n'

    def set_atributes(self):  # Изменяет данные пользователя
        print('\n============ Изменение данных пользователя ============\n' +
              'Введите новое значение или нажмите Enter для сохранения ' +
              'предыдущего значения')
        self.name = input('Изменить имя: ') or self.name
        proxy_height = input('Изменить рост (разделитель - точка): ')
        if proxy_height == '':
            pass
        else:
            self.height = float(proxy_height)
        proxy_weight = input('Изменить вес: ')
        if proxy_weight == '':
            pass
        else:
            self.weight = float(proxy_weight)
        proxy_age = input('Изменить возраст: ')
        if proxy_age == '':
            pass
        else:
            self.age = int(proxy_age)
        self.sex = input('Изменить пол: ') or self.sex
        print('Новые данные сохранены!')


USER_LIST = []
SCALE_START = 10
SCALE_END = 50


def user_registration():  # Производит регистрацию нового пользователя
    print('\n==== Регистрация пользователя ====')
    name = input('Пожалуйста, введите ваше имя: ')
    height = float(input('Ваш рост в метрах (разделитель - точка): '))
    weight = float(input('Ваша масса тела в килограммах: '))
    age = int(input('Введите ваш возраст: '))
    sex = input('Введите ваш пол (male/female): ')
    return name, height, weight, age, sex


def greetings():  # Приветственная заставка
    print('========== Калькулятор BMI ==========\n')
    print('Вас приветствует программа расчета индекса массы тела.\n')
    version = 'Текущая версия программы - v0.02, на данный момент доступен' + \
              ' следующий функционал:\n'\
              'Команда 1 - Добавление нового пользователя\n'\
              'Команда 2 - Просмотр списка пользователей, их данных ' + \
              'и рекомендаций\n'\
              'Команда 3 - Изменение данных пользователя\n'\
              'Команда 4 - Удаление пользователя\n'\
              'Команда 0 - Выход из программы'
    print(version)


def show_user_list():  # Выводит список зарегистрированных пользователей
    print('\n====== Список пользователей ======')
    if len(USER_LIST) == 0:
        print('\nНет зарегистрированных пользователей')
    else:
        for number in range(len(USER_LIST)):
            print(number+1, '-', USER_LIST[number].name)
        print('==================================\n')
        detailed_user_information()


def edit_user_list():  # Выбираем пользователя для изменения параметров
    print('\n====== Изменение пользователей ======')
    if len(USER_LIST) == 0:
        print('\nНет зарегистрированных пользователей')
    else:
        for number in range(len(USER_LIST)):
            print(number+1, '-', USER_LIST[number].name)
        print('==================================\n')
        request = int(input('Выберите пользователя по учетному номеру для ' +
                            'изменения данных.\nДля возврата в главное меню ' +
                            'нажмите любую кнопку.\nВведите команду: '))
        if 0 < request <= len(USER_LIST):
            USER_LIST[request-1].set_atributes()
            print('==================================')
        else:
            pass


def detailed_user_information():  # Выводит подробную ифнормацию пользователя
    request = int(input('Выберите пользователя по учетному номеру для ' +
                        'отображения данных.\nДля возврата в главное меню ' +
                        'нажмите 0.\nВведите команду: '))
    if 0 < request <= len(USER_LIST):
        print('\n==================================')
        print(USER_LIST[request-1].get_atributes(),
              USER_LIST[request-1].scale(),
              USER_LIST[request-1].recommendations())
        print('==================================')
    else:
        pass


def add_user():  # Добавление нового пользователя
    USER_LIST.append(Person(*user_registration()))


def delete_user():  # Удаляет пользователя из списка
    print('\n====== Удаление пользователей ======')
    if len(USER_LIST) == 0:
        print('\nНет зарегистрированных пользователей')
    else:
        for number in range(len(USER_LIST)):
            print(number+1, '-', USER_LIST[number].name)
        print('==================================\n')
        request = int(input('Выберите пользователя по учетному номеру для ' +
                            'его удаления.\nДля возврата в главное меню ' +
                            'нажмите любую кнопку.\nВведите команду: '))
        if 0 < request <= len(USER_LIST):
            USER_LIST.pop(request-1)
            print('Пользователь успешно удален!')
            print('==================================')
        else:
            pass


def main():  # Главное меню программы
    while True:
        print('\n========== Главное меню ==========')
        command = input('Введите номер команды: ')
        if command == '1':
            add_user()
            print ('Пользователь успешно зарегистрирован!')
        elif command == '2':
            show_user_list()
        elif command == '3':
            edit_user_list()
        elif command == '4':
            delete_user()
        elif command == '0':
            print('\nПрограмма завершена!\n')
            break
        else:
            print('Введена неверная команда, попробуйте еще раз!')


def mainloop():  # Основной цикл программы
    greetings()
    main()


if __name__ == '__main__':
    mainloop()

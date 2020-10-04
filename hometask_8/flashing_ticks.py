import time
import os
import datetime
from clock_numbers import *
from colorama import Fore

color_list = [Fore.RED,
              Fore.GREEN,
              Fore.YELLOW,
              Fore.BLUE,
              Fore.MAGENTA,
              Fore.CYAN,
              Fore.WHITE]


def color_decorator(func):  # Меняет цвет циферблата
    color_list_index = 0
    color_list_index_counter = 0

    def wrapper(*args):
        nonlocal color_list_index, color_list_index_counter
        color_list_index_counter += 1
        print(color_list[color_list_index])
        func(*args)
        if color_list_index_counter == 7:
            color_list_index_counter = 0
            if (color_list_index + 1 >= len(color_list) or
               color_list_index - 1 == -1):
                color_list_index = -color_list_index
            color_list_index += 1
        return func
    return wrapper


def generator():  # Мигалки на часах
    position_1 = [' ', ' ', SYMBOL, ' ', SYMBOL, ' ', ' ']
    position_2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    counter = 1
    while True:
        if counter == 28:
            counter = 0
        while counter <= 14:
            counter += 1
            yield position_1
        counter += 1
        yield position_2


def get_current_time():  # Получаем текущее время
    current_time = datetime.datetime.now()
    timelist = current_time.strftime('%H, %M, %S').split(', ')
    return timelist


@color_decorator
def drawing_clocks(current_time, tick):  # Отрисовываем часы
    timelist = current_time
    for i in range(7):
        print(numbers_dict[timelist[0][0]][i] + ' ' +
              numbers_dict[timelist[0][1]][i] + '\t' + next(tick)[i] + '\t' +
              numbers_dict[timelist[1][0]][i] + ' ' +
              numbers_dict[timelist[1][1]][i] + '\t' + next(tick)[i] + '\t' +
              numbers_dict[timelist[2][0]][i] + ' ' +
              numbers_dict[timelist[2][1]][i])


def main():  # Основной цикл программы
    tick = generator()
    while True:
        drawing_clocks(get_current_time(), tick)
        time.sleep(0.3)
        os.system('clear')


if __name__ == "__main__":
    main()

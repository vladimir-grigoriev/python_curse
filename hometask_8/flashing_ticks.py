import time
import os
import datetime
from clock_numbers import *


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
import time
import os
import datetime
from clock_numbers import *


def generator():  # Бегающие точки на часах
    position = [SYMBOL, ' ', ' ', ' ', ' ', ' ', ' ']
    counter = 0
    dx = 1
    while True:
        counter += 1
        yield position
        if counter - 14 == 0:
            counter = 0
            if position.index(SYMBOL)+dx >= len(position) or position.index(SYMBOL)+dx == -1:
                dx = -dx
            proxy = position[position.index(SYMBOL)]
            proxy_index = position.index(SYMBOL)
            position[proxy_index] = position[proxy_index+dx]
            position[proxy_index+dx] = proxy
            yield position


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
        time.sleep(0.05)
        os.system('clear')

if __name__ == "__main__":
    main()
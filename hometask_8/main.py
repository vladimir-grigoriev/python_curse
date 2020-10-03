# размер 5 х 7
from datetime import datetime
import time
from clock_numbers import *
import os


def get_current_time():  # Получаем текущее время
    current_time = datetime.now()
    timelist = current_time.strftime('%H, %M, %S').split(', ')
    return timelist


def drawing_clocks():  # Отрисовываем часы
    timelist = get_current_time()
    s = generator()
    for k in range(7):
        print(numbers_dict[timelist[0][0]][k] + ' ' + numbers_dict[timelist[0][1]][k] + '\t' + next(s)[k] + '\t' +
              numbers_dict[timelist[1][0]][k] + ' ' + numbers_dict[timelist[1][1]][k] + '\t' + next(s)[k] + '\t' +
              numbers_dict[timelist[2][0]][k] + ' ' + numbers_dict[timelist[2][1]][k])
    

def main():  # Основной цикл программы
    while True:
        drawing_clocks()
        time.sleep(2)
        os.system('clear')


if __name__ == "__main__":
    main()
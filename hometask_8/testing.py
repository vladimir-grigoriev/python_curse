import time
import os
import datetime

SYMBOL = '\u2588'

def generator():
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
s = generator()
def number_zero():  # Отрисовываем ноль
    zero = [
        ' ' + SYMBOL + SYMBOL + SYMBOL + ' ',
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        ' ' + SYMBOL + SYMBOL + SYMBOL + ' ',
    ]
    return zero
def number_one(): # Отрисовываем единицу
    one = [
        ' ' + ' ' + SYMBOL + ' ' + ' ',
        ' ' + SYMBOL + SYMBOL + ' ' + ' ',
        ' ' + ' ' + SYMBOL + ' ' + ' ',
        ' ' + ' ' + SYMBOL + ' ' + ' ',
        ' ' + ' ' + SYMBOL + ' ' + ' ',
        ' ' + ' ' + SYMBOL + ' ' + ' ',
        ' ' + SYMBOL + SYMBOL + SYMBOL + ' ',
    ]
    return one
def number_two(): # Отрисовываем двойку
    two = [
        ' ' + SYMBOL + SYMBOL + SYMBOL + ' ',
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        ' ' + ' ' + ' ' + ' ' + SYMBOL,
        ' ' + ' ' + ' ' + SYMBOL + ' ',
        ' ' + ' ' + SYMBOL + ' ' + ' ',
        ' ' + SYMBOL + ' ' + ' ' + ' ',
        SYMBOL + SYMBOL + SYMBOL + SYMBOL + SYMBOL,
    ]
    return two
def number_three(): # Отрисовываем тройку
    three = [
        SYMBOL + SYMBOL + SYMBOL + SYMBOL + SYMBOL,
        ' ' + ' ' + ' ' + SYMBOL + ' ',
        ' ' + ' ' + SYMBOL + ' ' + ' ',
        ' ' + ' ' + ' ' + SYMBOL + ' ',
        ' ' + ' ' + ' ' + ' ' + SYMBOL,
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        ' ' + SYMBOL + SYMBOL + SYMBOL + ' ',
    ]
    return three
def number_four(): # Отрисовываем четверку
    four = [
        ' ' + ' ' + ' ' + SYMBOL + ' ',
        ' ' + ' ' + SYMBOL + SYMBOL + ' ',
        ' ' + SYMBOL + ' ' + SYMBOL + ' ',
        SYMBOL + ' ' + ' ' + SYMBOL + ' ',
        SYMBOL + SYMBOL + SYMBOL + SYMBOL + SYMBOL,
        ' ' + ' ' + ' ' + SYMBOL + ' ',
        ' ' + ' ' + ' ' + SYMBOL + ' ',
    ]
    return four
def number_five(): # Отрисовываем пятерку
    five = [
        SYMBOL + SYMBOL + SYMBOL + SYMBOL + SYMBOL,
        SYMBOL + ' ' + ' ' + ' ' + ' ',
        SYMBOL + SYMBOL + SYMBOL + SYMBOL + ' ',
        ' ' + ' ' + ' ' + ' ' + SYMBOL,
        ' ' + ' ' + ' ' + ' ' + SYMBOL,
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        ' ' + SYMBOL + SYMBOL + SYMBOL + ' ',
    ]
    return five       
def number_six(): # Отрисовываем шестерку
    six = [
        ' ' + ' ' + SYMBOL + SYMBOL + ' ',
        ' ' + SYMBOL + ' ' + ' ' + ' ',
        SYMBOL + ' ' + ' ' + ' ' + ' ',
        SYMBOL + SYMBOL + SYMBOL + SYMBOL + ' ',
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        ' ' + SYMBOL + SYMBOL + SYMBOL + ' ',
    ]
    return six               
def number_seven():  # Отрисовываем семерку
    seven = [
        SYMBOL + SYMBOL + SYMBOL + SYMBOL + SYMBOL,
        ' ' + ' ' + ' ' + ' ' + SYMBOL,
        ' ' + ' ' + ' ' + SYMBOL + ' ',
        ' ' + ' ' + SYMBOL + ' ' + ' ',
        ' ' + SYMBOL + ' ' + ' ' + ' ',
        ' ' + SYMBOL + ' ' + ' ' + ' ',
        ' ' + SYMBOL + ' ' + ' ' + ' ',
    ]
    return seven
def number_eight():  # Отрисовываем восьмерку
    eight = [
        ' ' + SYMBOL + SYMBOL + SYMBOL + ' ',
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        ' ' + SYMBOL + SYMBOL + SYMBOL + ' ',
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        ' ' + SYMBOL + SYMBOL + SYMBOL + ' ',
    ]
    return eight
def number_nine():  # Отрисовываем девятку
    nine = [
        ' ' + SYMBOL + SYMBOL + SYMBOL + ' ',
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        SYMBOL + ' ' + ' ' + ' ' + SYMBOL,
        ' ' + SYMBOL + SYMBOL + SYMBOL + SYMBOL,
        ' ' + ' ' + ' ' + ' ' + SYMBOL,
        ' ' + ' ' + ' ' + SYMBOL + ' ',
        ' ' + SYMBOL + SYMBOL + ' ' + ' ',
    ]
    return nine

numbers_dict = {
    '0': number_zero(),
    '1': number_one(),
    '2': number_two(),
    '3': number_three(),
    '4': number_four(),
    '5': number_five(),
    '6': number_six(),
    '7': number_seven(),
    '8': number_eight(),
    '9': number_nine()
}
def get_current_time():  # Получаем текущее время
    current_time = datetime.datetime.now()
    timelist = current_time.strftime('%H, %M, %S').split(', ')
    return timelist
def drawing_clocks(current_time):  # Отрисовываем часы
    timelist = current_time
    for i in range(7):
        print(numbers_dict[timelist[0][0]][i] + ' ' + numbers_dict[timelist[0][1]][i] + '\t' + next(s)[i] + '\t' +
              numbers_dict[timelist[1][0]][i] + ' ' + numbers_dict[timelist[1][1]][i] + '\t' + next(s)[i] + '\t' +
              numbers_dict[timelist[2][0]][i] + ' ' + numbers_dict[timelist[2][1]][i])
        
while True:
    drawing_clocks(get_current_time())
    time.sleep(0.3)
    os.system('clear')

#while True:
#    for i in range(7):
#        print(number_two()[i] + '\t' + next(s)[i] + '\t' + number_one()[i] + '\t' + next(s)[i] + '\t' + number_two()[i])
#    time.sleep(0.3)
#    os.system('clear')

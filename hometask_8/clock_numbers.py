SYMBOL = '\u2588'


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
    '9': number_nine()}

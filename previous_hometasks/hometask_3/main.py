first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))

print('Задание 1. Выходное значение -', first_number and second_number and
      third_number and 'Нет нулевых значений!!!')

print('Задание 2. Выходное значение -', (first_number or second_number or
      third_number) or 'Введены все нули!')

print('Задание 3, 4. Выходное значение - ', first_number - second_number -
      third_number if first_number > second_number + third_number else
      second_number + third_number - first_number)

print('Задание 5. Выходное значение - ', 'Вася' if first_number > 50 and
      (first_number < second_number or first_number < third_number) else
      'Васю не выводим')

print('Задание 6. Выходное значение - ', 'Петя' if first_number > 5 or
      second_number + third_number == 7 else 'Петю не выводим')

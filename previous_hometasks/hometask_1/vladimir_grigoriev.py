def main():
    pattern = 'Не знаю, как там в Лондоне, я не была. Может, там собака '\
              '— друг человека. А у нас управдом — друг человека!'
    print(pattern)
    print()
    print('Задание 1. Количество символов - ' + str(len(pattern)))
    print()
    print('Задание 2. Развернутая строка: ' + pattern[::-1])
    print()
    print('Задание 3. Каждое слово с большой буквы: ' + pattern.title())
    print()
    print('Задание 4. Весь текст прописными буквами: ' + pattern.lower())
    print()
    print('Задание 5.')
    print('"нд" больше чем "ам":', str(bool(pattern.count('нд') > pattern.count('ам'))))
    print('"нд" больше чем "о":', str(bool(pattern.count('нд') > pattern.count('о'))))
    print('"ам" больше чем "о":', str(bool(pattern.count('ам') > pattern.count('о'))))
    print('"ам" больше чем "нд":', str(bool(pattern.count('ам') > pattern.count('нд'))))
    print('"о" больше чем "ам":', str(bool(pattern.count('о') > pattern.count('ам'))))
    print('"о" больше чем "нд":', str(bool(pattern.count('о') > pattern.count('нд'))))
    print()
    print('Задание 6. Собственные упражнения')
    print('Список слов:', pattern.split())
    print('Проверка на содержание цифр:', pattern.isdigit())
    print('Замена шаблона:', pattern.replace('Лондоне', 'Чертаново'))
    print('Нахождение позиции слова "друг":', pattern.find('друг'))



if __name__ == '__main__':
    main()    
my_string = input('Введите произвольный текст: ')
print("Количество символов  введенного текста:", len(my_string))
print('Введенная строка преобразована в верхний регистр: ', my_string.upper())
print('Введенная строка в нижнем регистре: ', my_string.lower())
print('Из введенной строки удалены все пробелы: ', my_string.replace(' ',''))
print('Первый символ введенной строки: ', my_string[0])
print('Последний символ введенной строки: ', my_string[-1])
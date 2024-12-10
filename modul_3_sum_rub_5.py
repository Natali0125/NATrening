#Когда в конце числа есть "0" - произведение всех чисел в итоге получается "0"
# В программу добавлен цикл для удаления всех нулей справа от введенного числа

def get_multiplied_digits(number):
    str_number = str(number)
    # НАЧАЛО: Цикл для удаления всех нулей в конце строки
    for i in range(len(str_number)):
        if str_number.endswith('0'):
            # print('в числе <str_number>  в конце "0"')
            str_number = str_number.rstrip('0')
            # print(type(str_number), str_number)
    # КОНЕЦ: цикла для удаления нулей в конце строки print(type(str_number), str_number)
            continue
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)


### 2 Вариант :Программа  с удалением  всех нулей справа от числа:
# #
def get_multiplied_digits(number):
    str_number = str(number)
    # НАЧАЛО: Цикл для удаления нулей в конце введенного числа
    for i in range(len(str_number)):
        if str_number.endswith('0'):
            str_number = int(str_number)
            str_number = int(str_number / 10)
            str_number = str(str_number)
            continue
    # КОНЕЦ: цикла для удаления нулей
        else:
            first = int(str_number[0])
            if len(str_number) > 1:
                return first * get_multiplied_digits(int(str_number[1:]))
            else:
                return first


result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)

result_3 = get_multiplied_digits(870887323000)
print(result_3)




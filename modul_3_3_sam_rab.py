def print_params(a = 1, b = 'text', c = True):
    print(a, b, c)

## 1) Вызов функции принт print_params с различным кол-ом аргументов:
#
print('1) Вызов без параметров ( параметры заданы по умолчанию):')
print_params() #
print('Задан только первый параметр: для "а" переопределено значение на 2:')
print_params(2) #
print('Заданы 2 параметра: переопределены "а" и "b"')
print_params(3, 'nwe_text') #
print('Заданы три параметра, каждый параметр изменил свой тип: a="ret", b=5, c=[2,7,9]')
print_params('ret', 5, [2, 7, 9]) #
print('(4) Задан  именованный парамет "b" = 25')
print_params(b = 25,) #
print('Задан именованный параметр с= [1, 2, 3]')
print_params(c = [1, 2, 3])

##
print('2) Распаковка параметров:')
value_list = ['sim', 7, [8, False, 'help']] # 1) создание списка с разными типами данных
values_dict ={'a' : 'list', 'b' : True, 'c' : [7, 'lit', True]} # 2) создание словаря с ключами и значениями разных
                                                            # типов, соответствующими параметрам функции print_params

print("Распаковка списка:['sim', 7, [8, False, 'help']] ")
print_params(*value_list)
print("Распаковка словаря: {'a' : 'list', 'b' : True, 'c' : [7, 'lit', True]} ")
print_params(**values_dict)


print('3) Распаковка + отдельные параметры:')

value_list_2 = ['Name', 12] # 1) Создание списка с двумя элементами разных типов данных
print('распаковка списка из 2х эл-ов+ параметр')
print_params(*value_list_2, 42)  # 2) Вывод на консоль:  Name 12 42
value_list_3 = [54.32, 'Строка' ]
print_params(*value_list_3, 42)


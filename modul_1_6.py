#Slovar'
my_dict = {'Alex' : 1980, 'Vlad' : 1975, 'Inna' : 2000}
print('Первый вариант словаря: ',my_dict)
print("Значение ключа 'Vlad': ", my_dict['Vlad'])
print("Запрос ключа 'Ivan':", my_dict.get('Ivan', 'Такого ключа нет'))
my_dict.update({'Svetlana' : 1960,
                   'Sasha' : 2005})
d = my_dict.pop('Vlad')
print("Значение удаленного ключа'Vlad': ", d)
print('Новый вариант словаря', my_dict)
# Mnozestva
my_set = {89, 14, 89, 'liter', 5, 25, 5, (7, False, 'sun')}
print('Множество: ', my_set)
my_set.add(56)
#print('Добавление элемента (56) в множество: ', my_set)
my_set.add('old')
#print("Добавление элемента 'old': ", my_set)
my_set.discard((7, False, 'sun'))
print('Измененное множество: ', my_set)

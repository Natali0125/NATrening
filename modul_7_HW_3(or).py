# Домашнее задание по теме "Позиционирование в файле"
# Задача "Записать и запомнить"
import io

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

def custom_write(file_name, strings):
    rez = []
    nstr = 0
    poz_curs = 0
    list_tup = []
    tup = ()

    file = open(file_name, 'a', encoding = 'utf-8')
    for i in strings:
        poz_curs = file.tell()
        file.write(i.__str__() + '\n')
        rez.append(i)
        nstr += 1
        tup = nstr, poz_curs
        list_tup.append(tup)

        result = dict(zip(list_tup, rez))
    file.close()
    return result


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

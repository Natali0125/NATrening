# Домашнее задание по теме "Оператор "with"
# Задача "Найдёт везде"
import re
import string


class  WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.get_all_words()

     # подготовительный метод, который возвращает словарь: "имя файла": [список слов в файле]
    def get_all_words(self):
        all_words = {}
        f_all_word = '' # Переменная для вывода текста из файла
        list_all_word = []
            # чтение текста из файла в переменную. Вывод  текста маленькими буквами
        for file_name in self.file_names:
            with open(file_name, 'r', encoding = 'utf-8') as file:
                f_all_word = file.read().lower() # Вывода текста в переменную из файла

                #  удаление из текста знаков препинания
            dict_sim = {',': '', '.': '', '=': '', '!': '', '?': '', ';': '', ':': '', ' - ': ' '}
            for char in dict_sim.keys():
                f_all_word = f_all_word.replace(char, dict_sim[char])
            list_all_word = f_all_word.split() # Преобразование текста в список
            all_words[file_name] = list_all_word  # Словарь - Имя файла: содержимое файла

            #     # Второй вариан удаления из текста знаков препинания
            # new_f_all_word = re.sub(r'[\=\?\!\,\.\;\:\"]', '', f_all_word.lower())
            # list_all_word = (re.sub(' - ', ' ', new_f_all_word)).split()
        return all_words    # all_words - словарь с отсортированными словами из текста в список
        # Функция для поиска слова и определения позиции в списке
    def find(self, word):
        word_in = {} # Переменная для вывода словаря: "имя файла" : [позиция вхождения слова]
        word = word.lower()
        index_word = 0 # Переменная для вывода индекса найденного слова
        for name, list_text in self.get_all_words().items():

            for words_l in list_text:
                if word in list_text:
                    index_word = list_text.index(word)
                    index_word = index_word +1 # Добавляется единица, чтоб отразить позицию в списке, а не индекс
                    word_in[name] = index_word
                    #continue
        return word_in

    def count(self, word):
        find_word = {} # Словарь для вывода информации: "Имя файла" : [количество вхождений найденного слова]
        word = word.lower()

        for name, list_text in self.get_all_words().items():
            count_word = 0 # Переменная для вывода количества нахождений
            for words_l in list_text:
                if word in list_text:
                    count_word = list_text.count(word)
                    find_word[name] = count_word

        return find_word


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту

print(finder2.count('teXT')) # 4 слова teXT в тексте всего









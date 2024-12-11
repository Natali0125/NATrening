# Самостоятельная работа по уроку "Произвольное число параметров"
# черновик домашнего задания
#
def single_root_words(root_word = 'rICh', *other_words):
    print()
    same_words = []
    root_word = root_word.lower()
    for i in range(len(other_words)):
        other_words_l = other_words[i].lower()
        if root_word.lower().count(other_words_l) == 1:
            same_words.append(other_words[i])
            continue
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)
    return same_words

rezult_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
rezult_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(rezult_1)
print(rezult_2)

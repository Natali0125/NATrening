

calls = 0

def count_calls():
    global calls
    calls += 1
    #print('Количество вызовов:', colls)
    return calls
#
def string_info(text):
    count_calls()
    #print(text.upper())
    #print(text.lower())
    tuple_1 = len(text), text.upper(), text.lower()   # c, d
    #print('Длина строки', len(text))
    return tuple_1

def is_contains(text_1, list_1 =[]):
    count_calls()
    text_1 = text_1.upper()
    list_1_1 = []
    for i in range(len(list_1)):
        l_1 = list_1[i].upper()
        list_1_1.append(l_1)
    return text_1 in list_1_1



print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)



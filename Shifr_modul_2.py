
    # Поиск шифра
key_ = ''
print()
c = int(input('Введите целое число от 3 до 20 (включительно): '))
#if с <= 2 or с >= 21:
 #   print('Введено некорректное число')
for i in range(1, c):
    for j in range(i+1, c+1):
        s = i + j
        if c % s == 0:
            key_ += str(i) + str(j)
            # key_.append(i)
            # key_.append(j)
print('Ключ для выхода из ловушки: ', key_)


###
# Второй вариант  поиска ключа с помощью функции

def find_key(k):
    key_ = ''
    #print('Ключ до цикла', key_)
    for i in range(1, k+1):
        for j in range(i+1, k+1):
            if k % (i + j) == 0:
                key_ += str(i) + str(j)
    return key_

print()
shifr = (find_key(int(input('Введите целое число от 3 до 20 (включительно): '))))
print(shifr)




'''  
    # Ключи для проверки
    
    # ключ для 3    - 12
    # ключ для 4    - 13
    # ключ для 5    - 1423
    # ключ для 6    - 121524
    # ключ для 7    - 162534
    # ключ для 8    - 13172635
    # ключ для 9    - 1218273645  
    # ключ для 10   - 141923283746
    # ключ для 11   - 11029384756
    # ключ для 12   -12131511124210394857
    # ключ для 13   - 112211310495867
    # ключ для 14   - 1611325212343114105968
    # ключ для 15   - 1214114232133124115106978
    # ключ для 16   - 1317115262143531341251161079
    # ключ для 17   - 11621531441351261171089
    # ключ для 18   - 12151811724272163631545414513612711810
    # ключ для 19   - 118217316415514613712811910
    # ключ для 20   - 13141911923282183731746416515614713812911   
'''


first = float(input('Введите первое целое число: '))
second = float(input('Введите второе целое число: '))
third = float(input('Введите третье целое число: '))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)

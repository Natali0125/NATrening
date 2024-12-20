def divide(first, second):
    if second == 0:
        return f'Ошибка'
    res = first/second
    return res


def main():
    print("Привет, это модуль <fake_math> :!)" )
    res_1 = divide(6, 0)
    print(res_1)
    res_2 = divide(17, 0)
    print(res_2)

if __name__ == '__main__':
    main()

#print(__name__)




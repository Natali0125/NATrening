import math
from math import inf

def divide(first, second):
    if second == 0:
        return math.inf

    res = first/second
    return res


def main():
    print("Привет, это модуль <true_math> :!)" )
    res_1 = divide(6, 0)
    print(res_1)
    res_2 = divide(17, 0)
    print(res_2)
    res_2 = divide(8, 0)
    print(res_2)

if __name__ == '__main__':
    main()

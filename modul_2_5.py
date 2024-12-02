def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        a = []
        matrix.append(a)
        for j in  range(m):
            a.append(value)
            # после всез циклов вернуть значение матрикс
    return matrix

rezult_1 = get_matrix(2,2,10)
rezult_2 = get_matrix(3, 5, 42)
rezult_3 = get_matrix(4, 2, 13)

print(rezult_1)
print(rezult_2)
print(rezult_3)



def get_matrix(n, m, value):
    matrix = [] # по-условию
    for i in range(n): # принимается значение n для пустого списка?
        matrix_ = []
        for j in range(m): # принимается значение m
            matrix_.append(value) # добавляем третье значение
        matrix.append(matrix_) #добавляем вложенный список в первый пустой список

    return matrix

result1 = get_matrix(2,2,10)
print(result1)
result2 = get_matrix(3, 5, 42)
print(result2)
result3 = get_matrix(4, 2, 13)
print(result3)
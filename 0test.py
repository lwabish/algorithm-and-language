def square_matrix_multiply(m1, m2):
    dimension = len(m1)
    new_matrix = [[0]*dimension for i in range(dimension)]
    for row in range(dimension):
        for column in range(dimension):
            sum = 0
            this_row = m1[row]
            this_colmn = [every_row[column] for every_row in m2]
            for i in range(len(this_row)):  # 迭代矩阵的第raw行
                for j in range(len(this_colmn)):  # 迭代矩阵的第column列
                    if i == j:
                        sum += this_row[i] * this_colmn[j]
            new_matrix[row][column] = sum
    return new_matrix


test = [[1, 1], [1, 0]]
print(square_matrix_multiply(test, test))

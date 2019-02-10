
# 自下而上的实现：先求1，2，再求3……直到求到目标值


def main(n):
    result_list = [0, 1]
    if n < 2:
        return result_list[n]
    for i in range(n - 1):
        new_sum = result_list[i] + result_list[i + 1]
        result_list.append(new_sum)
    return result_list[-1]


# 矩阵的n-1次方解法，结合二分法递归，时间复杂度logn
def main2(n):
    fib_matrix = [[1, 1], [1, 0]]

    # 方阵相乘
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

    def generate_e_matrix(n):
        e_matrix = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    e_matrix[i][j] = 1
        return e_matrix
    # 矩阵阶乘函数---二分法递归求解

    def matrix_pow(matrix, x):
        if len(matrix) != len(matrix[0]):
            return '该矩阵无法求幂'
        if x == -1:
            return [[0]]
        if x == 0:
            return generate_e_matrix(len(matrix))
        if x == 2:
            return square_matrix_multiply(matrix, matrix)
        if x == 3:
            return square_matrix_multiply(matrix_pow(matrix, 2), matrix)
        if x % 2 == 1:  # 奇数次幂
            return square_matrix_multiply(matrix_pow(matrix_pow(matrix, (x - 1) / 2), 2), matrix)
        else:  # 偶数次幂
            return matrix_pow(matrix_pow(matrix, x/2), 2)
    return matrix_pow(fib_matrix, n-1)[0][0]


if __name__ == '__main__':
    tc = 0
    while tc < 100:
        print(main(tc))
        print(main2(tc))
        tc += 1

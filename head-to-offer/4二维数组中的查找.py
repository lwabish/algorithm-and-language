# 二维数组查找算法

tc = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]  # 正常矩阵
target = 7  # 内部存在的值
target = 9  # 在矩阵边界存在的值
target = 100  # 矩阵外部不存在的值
target = 3  # 内部不存在的值

tc = [[0]]  # 边界矩阵
target = 0
target = 1
target = -1

tc = [[]]
target = 1


def main(matrix, target):
    if len(matrix) < 1:
        return -1
    if len(matrix[0]) < 1:
        return -1

    def cut_matrix(x, y):
        """
        xy是从**左下角**算留下的行和列数
        返回切片后的二维矩阵
        """
        matrix_x = matrix[len(matrix)-x:]  # 先按行截取
        matrix_y = [line[0:y] for line in matrix_x]  # 再对每行截取列
        return matrix_y
    # print(cut_matrix(3, 2))
    x_total, possible_x = len(matrix), len(matrix)
    possible_y = len(matrix[0])
    possilbe_matrix = cut_matrix(possible_x, possible_y)
    # print(possilbe_matrix)
    result = -1
    while len(possilbe_matrix) >= 1 and len(possilbe_matrix[0]) >= 1:
        # print(len(possilbe_matrix), len(possilbe_matrix[0]))
        possilbe_matrix_right_top_value = possilbe_matrix[0][-1]
        if possilbe_matrix_right_top_value == target:
            result = [x_total-possible_x, possible_y-1]
            break
        if possilbe_matrix_right_top_value > target:
            possible_y -= 1
            possilbe_matrix = cut_matrix(possible_x, possible_y)
            # print(possilbe_matrix)
        if possilbe_matrix_right_top_value < target:
            possible_x -= 1
            possilbe_matrix = cut_matrix(possible_x, possible_y)
            # print(possilbe_matrix)
    return result


if __name__ == '__main__':
    print(main(tc, target))

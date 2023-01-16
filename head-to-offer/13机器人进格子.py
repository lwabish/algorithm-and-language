from my_data_structure import get_digit_sum, print_matrix

# 正常测试用例
tc_dimension = (10, 10)
tc_k = 3
# 特殊矩阵
tc_dimension = (1, 15)
tc_k = 4
tc_k = 0
tc_k = -1


def main(m, n, k):
    matrix = [['-'] * n for _ in range(m)]
    q = {(0, 0)}
    already_used = [[False]*n for _ in range(m)]

    def go():
        def append_neighbor():
            if x - 1 in range(len(matrix)) and not already_used[x - 1][y]:
                q.add((x - 1, y))
            if x + 1 in range(len(matrix)) and not already_used[x + 1][y]:
                q.add((x + 1, y))
            if y - 1 in range(len(matrix[0])) and not already_used[x][y - 1]:
                q.add((x, y - 1))
            if y+1 in range(len(matrix[0])) and not already_used[x][y + 1]:
                q.add((x, y + 1))
        # print(q)
        if not q:
            return
        this_point = q.pop()
        x = this_point[0]
        y = this_point[1]
        # print_matrix(already_used)
        already_used[x][y] = True
        if get_digit_sum(x) + get_digit_sum(y) <= k:
            matrix[x][y] = '*'
            append_neighbor()
        go()
    go()
    return matrix


if __name__ == '__main__':
    print_matrix(main(tc_dimension[0], tc_dimension[1], tc_k))

from my_data_structure import print_matrix, generate_matrix

# 正常用例
tc_matrix = generate_matrix('abtgcfcsjdeh', 3, 4)
tc_target_string = 'abtgscfdeh'
# 单行单列矩阵
tc_matrix = generate_matrix('abcd', 4, 1)
tc_target_string = 'abcd'
tc_matrix = generate_matrix('abcd', 1, 4)
tc_target_string = 'abcd'
# 单值矩阵
tc_matrix = generate_matrix('a', 1, 1)
tc_target_string = 'a'
tc_target_string = 'b'


def main(matrix, target):
    # 多少行
    x = len(matrix)
    # 多少列
    y = len(matrix[0])
    # bool矩阵，用来标记是否已经进入过
    already_used = [[False]*y for _ in range(x)]
    # 每层可以探索的子节点坐标
    availible = [[] for _ in range(len(target))]
    availible[0] = [(matrix.index(line), line.index(point))
                    for line in matrix for point in line]

    def next_move(depth):

        def append_neighbor():
            """
            将当前点的可用邻居加入下一层，等待匹配
            """
            # 为了防止对矩阵边界点测试时下标越界，判断时要先判断x+-1,y+-1是否有效，如果有效再进行后续判断和操作。python的布尔测试在遇到第一个条件不满足时会停止判断后面的条件。
            if y - 1 in range(len(matrix[0])) and not already_used[x][y - 1]:
                availible[depth + 1].append((x, y - 1))
            if y + 1 in range(len(matrix[0])) and not already_used[x][y+1]:
                availible[depth+1].append((x, y + 1))
            if x - 1 in range(len(matrix)) and not already_used[x-1][y]:
                availible[depth+1].append((x - 1, y))
            if x + 1 in range(len(matrix)) and not already_used[x + 1][y]:
                availible[depth+1].append((x + 1, y))

        print('___________________________')
        print('当前深度：', depth,)
        print_matrix(availible)
        print_matrix(already_used)

        if not [i for t in availible for i in t]:  # false基线条件
            return False

        if depth > 0 and not availible[depth]:  # 回退上一层的条件
            print('该层没有结果，退回上层')
            depth -= 1
            # already_used[x][y] == False  # 是否有不同子树重复进入同一格的可能性？
            return next_move(depth)

        cordinate = availible[depth].pop()
        x = cordinate[0]
        y = cordinate[1]
        this_str = matrix[x][y]
        print('当前测试：', cordinate, this_str)

        if this_str == target[depth]:  # 找到了当前层的匹配字符
            print('在第{}层找到匹配的字符'.format(depth))

            if depth == len(target) - 1:   # true基线条件
                return True

            append_neighbor()
            already_used[x][y] = True

            # 递归进入下一层
            depth += 1
            return next_move(depth)
        else:
            print('与{}不匹配，继续在第{}层寻找'.format(target[depth], depth))
            return next_move(depth)
    return next_move(0)


if __name__ == '__main__':
    print(main(tc_matrix, tc_target_string))

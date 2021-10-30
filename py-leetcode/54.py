from typing import List
tcs = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
    ([[2, 3]],),
    ([[1], [2]],),
    ([[1]],),
]


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 算出矩阵元素总数，作为循环的终止标记
        m, n = len(matrix), len(matrix[0])
        if m == 1:
            return matrix[0]
        result_indexes = []
        # 初始化方向变量，方向变量按照 右0 下1 左2 上3 右4 的顺序循环，每次+1
        # 读的时候除4取余判断方向
        direction = 0
        # 初始化矩阵索引变量
        i, j = 0, 0
        while len(result_indexes) < m*n:
            result_indexes.append((i, j))
            # 确定下一个矩阵坐标的索引
            # 首先确定是不是要转方向
            # 两种情况需要转方向，根据下一个坐标：
            # 1.到头了
            # 注意是m-1 n-1
            if (i, j) == (0, n-1) or (i, j) == (m-1, n-1) or (i, j) == (m-1, 0):
                direction += 1
            # 2.下一个坐标已经在result_indexes里了
            if direction % 4 == 0 and (i, j+1) in result_indexes:
                direction += 1
            elif direction % 4 == 1 and (i+1, j) in result_indexes:
                direction += 1
            elif direction % 4 == 2 and (i, j-1) in result_indexes:
                direction += 1
            elif direction % 4 == 3 and (i-1, j) in result_indexes:
                direction += 1

            # 根据方向，确定下一个坐标的索引
            if direction % 4 == 0:
                j += 1
            elif direction % 4 == 1:
                i += 1
            elif direction % 4 == 2:
                j -= 1
            elif direction % 4 == 3:
                i -= 1
        print(result_indexes)
        return list(map(lambda x: matrix[x[0]][x[1]], result_indexes))


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.spiralOrder(*tc))

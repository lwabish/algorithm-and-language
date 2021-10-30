from typing import List
tcs = [
    (3,),
    (1,),
]


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 坐标和值的hash
        point_value = {}
        result = [[-1]*n for i in range(n)]
        direction = 0
        i, j = 0, 0
        while len(point_value) < n*n:
            # 填充坐标和值的map
            point_value[(i, j)] = len(point_value)+1

            # 转向1：
            if (i, j) == (0, n-1) or (i, j) == (n-1, n-1) or (i, j) == (n-1, 0):
                direction += 1
            # 转向2：
            if direction % 4 == 0 and (i, j+1) in point_value:
                direction += 1
            elif direction % 4 == 1 and (i+1, j) in point_value:
                direction += 1
            elif direction % 4 == 2 and (i, j-1) in point_value:
                direction += 1
            elif direction % 4 == 3 and (i-1, j) in point_value:
                direction += 1

            # 下一个点
            if direction % 4 == 0:
                j += 1
            elif direction % 4 == 1:
                i += 1
            elif direction % 4 == 2:
                j -= 1
            elif direction % 4 == 3:
                i -= 1

        # 把map转化成矩阵
        # print(point_value)
        for o, p in point_value:
            result[o][p] = point_value[(o, p)]
        return result


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.generateMatrix(*tc))

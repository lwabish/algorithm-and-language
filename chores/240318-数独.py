from typing import List
tcs = [
    ([[1, 2, 3], [1, 2, 3], [1, 2, 3]]),
]


class Solution:
    def judge(self, matrix):
        n = len(matrix)
        # 判断行
        for line in matrix:
            if not self.right(line):
                return False
        # 判断列
        for line in matrix:
            column = []
            for j in range(len(n)):
                column.append(line[j])
            if not self.right(column):
                return False
        # 判断子矩阵
        for i in range(len(n)):
            if i > 6:
                continue
            for j in range(len(n)):
                if j > 6:
                    continue
                subMatrix = self.buildSubMatrix((i, j),)
                if not self.right(subMatrix):
                    return False
        return True

    def right(self, l):
        nums = set(l)
        return len(nums) == 9

    # 根据左上角定点确定一个3*3的矩阵
    def buildSubMatrix(self, m, point):
        result = []
        x, y = point[0], point[1]
        for i in range(3):
            for j in range(3):
                result.append(m[x+i][y+j])
        return result


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.judge(*tc))

from typing import List
tcs = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],),
]


# 难点计算公式：每个柱子可以接到水的量为：leftMax rightMax的最小值和自身柱高的差
class Solution_DP:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        for k, e in enumerate(height):
            if len(leftMax) == 0:
                leftMax.append(e)
                continue
            leftMax.append(max(e, leftMax[k-1]))
        rightMax = []
        for k, e in enumerate(height[::-1]):
            if len(rightMax) == 0:
                rightMax.append(e)
                continue
            rightMax.append(max(e, rightMax[k-1]))
        rightMax.reverse()

        result = 0
        for k, e in enumerate(height):
            result += min(leftMax[k], rightMax[k])-e
            print(k, e, leftMax[k], rightMax[k], result)
        return result


if __name__ == '__main__':
    solution = Solution_DP()
    for tc in tcs:
        print(solution.trap(*tc))

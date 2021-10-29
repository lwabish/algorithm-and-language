from typing import List
tcs = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7],),
    ([0, 0],),
    ([1, 0],),
]


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        容器(坐标直线围成面积)的最大值
        双指针
        难点在于想到从指针的变动对面积的影响出发
        """
        l, r = 0, len(height)-1
        result = 0
        while l < r:
            s = (r-l)*min(height[l], height[r])
            if s > result:
                result = s
            # 结束后指针内移
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.maxArea(*tc))

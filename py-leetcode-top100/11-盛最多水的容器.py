from typing import List
tcs = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7],),
]


# 暴力：on2复杂度太高
class Solution_Violent:
    def maxArea(self, height: List[int]) -> int:
        max_square = 0
        for l in range(len(height)):
            r = l+1
            while r < len(height):
                s = (r-l)*min(height[l], height[r])
                max_square = max(s, max_square)
                r += 1
        return max_square


# 双指针（对撞指针）
# 这题的难点是思路，需要知道这个事实：以对撞指针的模式去找更大面积时，更大的面积只能出现在向内移动小指针的过程中
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_square = 0
        l, r = 0, len(height)-1
        while l < r:
            max_square = max(max_square, (r-l)*min(height[l], height[r]))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_square


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.maxArea(*tc))

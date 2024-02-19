from typing import List
tcs = [
    ([0, 1, 0, 3, 12],),
]


# 快指针找不为零的数
# 慢指针标记坑的位置
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if i != s:
                nums[i], nums[s] = nums[s], nums[i]
            s += 1


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        solution.moveZeroes(*tc)
        print(tc)

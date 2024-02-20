from typing import List
tcs = [
    ([1, 2, 3, 4, 5, 6, 7], 3),
]


# 巧妙的方法：三次旋转
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.rotate(*tc))

from typing import List
tcs = [
    ([0, 1, 0, 3, 12],),
]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        insert_i = 0
        while index < len(nums):
            if nums[index]:
                nums.insert(insert_i, nums.pop(index))
                insert_i += 1
            index += 1


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        solution.moveZeroes(*tc)
        print(tc[0])

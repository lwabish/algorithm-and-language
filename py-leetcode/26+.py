from typing import List
tcs = [
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],),
    ([1, 1],),
    ([1, 2],),
]


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        排序数组原地去重
        双指针
        writer指针是慢指针，负责覆写
        scanner指针遍历数组，扫描每个不一样的数字
        """
        if len(nums) < 2:
            return len(nums)
        writer, scanner = 1, 1
        while scanner <= len(nums)-1:
            if nums[scanner] > nums[scanner-1]:
                nums[writer] = nums[scanner]
                writer += 1
            scanner += 1
        # print(nums)
        return writer


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.removeDuplicates(*tc))

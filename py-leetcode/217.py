from typing import List
tcs = [
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],),
]


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        数组里是否存在重复元素
        基于哈希判断
        """
        return len(nums) != len(set(nums))


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.containsDuplicate(*tc))

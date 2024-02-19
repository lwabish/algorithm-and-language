from typing import List
tcs = [
    ([2, 7, 11, 15], 9),
]


# 哈希
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            minus = target-nums[i]
            if minus in m:
                return [i, m[minus]]
            m[nums[i]] = i


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.twoSum(*tc))

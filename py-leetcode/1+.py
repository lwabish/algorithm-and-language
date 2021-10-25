from typing import List
tcs = [
    ([2, 7, 11, 15], 9),
    ([3, 3], 6),
]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        scanned = {}
        for key, num in enumerate(nums):
            if (target-num) in scanned:
                return [key, scanned.get(target-num)]
            scanned[num] = nums.index(num)
        return [0, 0]


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.twoSum(*tc))

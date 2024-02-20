from typing import List
tcs = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4],),
]


# 动态规划
# 难点：状态转移
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp, result = [nums[0]], nums[0]
        for k, e in enumerate(nums[1:]):
            dp_new = e+dp[k] if dp[k] > 0 else e
            dp.append(dp_new)
            result = max(result, dp_new)
        return result


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.maxSubArray(*tc))

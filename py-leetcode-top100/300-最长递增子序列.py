from typing import List
tcs = [
    ([10, 9, 2, 5, 3, 7, 101, 18],),
    ([0, 1, 0, 3, 2, 3],),
]


class Solution:
    # 动态规划，面试时想到了关注尾巴，但是没想到完整的算法
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1]
        for i, v in enumerate(nums):
            if i == 0:
                continue
            m = 1
            for j in range(i):
                if v > nums[j]:
                    m = max(m, dp[j]+1)
            dp.append(m)
        return max(dp)

    # 这是在面试中想的方法
    # 这种方法不是真正的暴力
    # 同时这种方法是错的，比如对于[0, 1, 0, 3, 2, 3]
    def wrong_way(self, nums):
        n = len(nums) - 1
        res = 0
        for i in range(n):
            l = 1
            m = nums[i]
            for j in range(i+1, n):
                # 不能通过这个条件判断，会影响后面
                # 比如m=3时，后面还有2,3的更优解
                if nums[j] > m:
                    m = nums[j]
                    l += 1
                res = max(res, l)
        return res

    # 真正的暴力：生成所有子序列，判断是否递增，是的话更新最大值
    def violence(self, nums):
        pass


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.lengthOfLIS(*tc))

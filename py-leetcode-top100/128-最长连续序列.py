from typing import List
tcs = [
    ([100, 4, 200, 1, 3, 2],),
]


# 哈希
# 使用set将数组哈希化，这样可以o1找到一个数是否存在
# 如果一个数不是序列里的最小数，可以直接跳过，我们只针对序列的最小数进行测试匹配即可避免重复测试
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)

        for n in nums:
            if n-1 in num_set:
                continue

            l = 1
            t = n
            while t + 1 in num_set:
                t = t + 1
                l += 1
            if l > max_len:
                max_len = l
        return max_len


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.longestConsecutive(*tc))

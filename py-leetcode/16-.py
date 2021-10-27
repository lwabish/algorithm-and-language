from typing import List
tcs = [
    ([-1, 2, 1, -4], 1),
    ([0, 0, 0], 1),
    ([0, 2, 1, -3], 1),
    ([1, 2, 4, 8, 16, 32, 64, 128], 82),
    ([1, 2, 5, 10, 11], 12),
]


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        和target最近的三数之和，len(nums)>=3
        因为要找到最近的，所以必须遍历
        易错点：必须全部遍历，不能像15题里跳过部分。因为遍历点的增大只意味着和变大，但并不意味着和target的差一定变大。
        易错点：什么时候需要check并更新result？少了会漏掉真值，多了可能会把双指针重合时的和包括进去。
        """
        result = float("inf")
        nums.sort()
        for i, v in enumerate(nums):
            if i == len(nums)-2:
                break
            l, r = i+1, len(nums)-1
            while l < r-1:
                s = nums[l]+nums[r]+v
                if abs(s-target) < abs(result-target):
                    result = s
                if s == target:
                    return target
                elif s > target:
                    r -= 1
                elif s < target:
                    l += 1
            # 因为一开始加了while循环后的一次check，所以会把双指针重合时的结果包括进去，所以while的条件要由l<r变成l<r-1
            s = nums[l]+nums[r]+v
            if abs(s-target) < abs(result-target):
                result = s
        return result


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.threeSumClosest(*tc))

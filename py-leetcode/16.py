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
            # while循环是一定能进来的！所以不需要在for循环里加check result
            while l < r:
                s = nums[l]+nums[r]+v
                ##################################
                # 每次while开始时检测一次，后面的是收尾操作
                if abs(s-target) < abs(result-target):
                    result = s
                ##################################

                if s == target:
                    return target
                elif s > target:
                    r -= 1
                elif s < target:
                    l += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.threeSumClosest(*tc))

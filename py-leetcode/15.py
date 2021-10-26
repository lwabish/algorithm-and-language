from typing import List
tcs = [
    ([-1, 0, 1, 2, -1, -4],),
    ([0, 0, 0],),
]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        三数之和等于零
        双指针法：对排序后的数组遍历，定1动2
        """
        if len(nums) < 3:
            return []
        result = []
        # 先排序
        nums.sort()
        for i, v in enumerate(nums):
            # 优化点：遍历点是一个正数时，因为已经排序，右边的数都更大，不可能相加为零
            if v > 0:
                break
            # 去重：遍历点数字重复时，结果也是重的，跳过
            if i-1 >= 0 and nums[i-1] == v:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l]+nums[r] == -1*v:
                    result.append([v, nums[l], nums[r]])
                    # 去重：指针向内收缩，跳过重复值
                    l, r = self.skipSameValue(l, r, nums)
                    # 易错：去重完后仍然要保证双指针内缩，不然会死循环
                    l += 1
                    r -= 1
                elif nums[l]+nums[r]+v > 0:
                    r -= 1
                elif nums[l]+nums[r]+v < 0:
                    l += 1
        return result

    def skipSameValue(self, l, r, nums):
        """
        向内移动l和r到重复值的边缘（即保证下一次移动后的值一定是不重复的）
        注意避免越界
        """
        while l + 1 <= len(nums)-1 and nums[l+1] == nums[l]:
            l += 1
        while r-1 >= 0 and nums[r-1] == nums[r]:
            r -= 1
        return l, r


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.threeSum(*tc))

from typing import List
tcs = [
    ([3, 1], 1),
    ([4, 5, 6, 7, 8, 9, 0, 1], 5),
    ([4, 5, 6, 7, 8, 9, 0, 1], 0),
    ([8, 9, 0, 1, 2, 3, 4, 5], 5),
    ([8, 9, 0, 1, 2, 3, 4, 5], 0),
    ([1], 0),

]


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        搜索旋转排序数组
        难点：思路以及边界条件
        1. nums[0] nums[len(nums)-1]
        2. 等号
        """
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            # 左边是连续的
            # 易错：跟nums[0]比而不是跟nums[l]比
            if nums[mid] >= nums[0]:
                if nums[0] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            # 右边是连续的
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    l = mid+1
                else:
                    r = mid-1
        return -1


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.search(*tc))

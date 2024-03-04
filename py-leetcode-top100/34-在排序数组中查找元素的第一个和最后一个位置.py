from typing import List
tcs = [
    ([5, 7, 7, 8, 8, 10], 8),
    ([0], 0),
    ([], 0),
]


# 技巧：二分查找如何找区间
# 在基本的二分查找的基础上，稍作改动即可实现查找左右边界
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]

        # 寻找左边界
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = int((l+r)/2)
            if nums[mid] == target:
                # 找到后更新左边界
                result[0] = mid
                # 但是不要返回，继续往左找，逼近真正的左边界
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        # 寻找右边界
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = int((l+r)/2)
            if nums[mid] == target:
                # 找到后更新右边界
                result[1] = mid
                # 但是不要返回，继续往右找，逼近真正的右边界
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return result


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.searchRange(*tc))

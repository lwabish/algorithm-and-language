from typing import List
tcs = [
    ([1, 3, 5, 6], 5),
    ([1, 3, 5, 6], 2),
    ([1, 3, 5, 6], 7),
    ([1, 3, 5, 6], 0),
]


# 移动左右指针的时候记得+-1，否则最后一轮会死循环
# while循环的条件加上=，实际上是在判断最后的结果l是否需要加1
# 自然语言：在二分查找的基础上，把查找目标从相等，改为了查找第一个比目标大或相等的数
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = int((r+l)/2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return l


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.searchInsert(*tc))

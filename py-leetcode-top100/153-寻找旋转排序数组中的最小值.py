from typing import List
tcs = [
    ([4, 5, 6, 7, 0, 1, 2],),
    ([2, 1],)
]


# 思路我想到了：最小值一定存在于非连续区间里
# 通过二分查找，不断缩小区间，将区间缩小至包含旋转点在内的2/3元数组
# 难点：普通的二分每次挪动左右指针时都是+1 -1，但是这个题里移动时不对称
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while nums[l] > nums[r]:
            mid = int((l+r)/2)
            # 左侧是连续区间
            if nums[l] <= nums[mid]:
                l = mid+1
            else:
                r = mid
        return nums[l]


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.findMin(*tc))

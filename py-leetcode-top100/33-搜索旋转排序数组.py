from typing import List
tcs = [
    ([4, 5, 6, 7, 0, 1, 2], 3),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([3, 1], 1)
]


# 旋转数组有什么重要特性？ nums[l]>nums[r]
# 所以通过这个可以明确判断出任何一个子区间是否是连续数组
# 进而尝试把问题转化成普通的二分
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = int((l+r)/2)

            # 终止条件：如果我们已经把问题转换成了顺序区间的二分查找
            if nums[l] <= nums[r]:
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 如果问题不是顺序区间，我们要尝试转化
            else:
                # 左区间是连续的且target在里面，那我们可以很容易地把问题转化成普通的二分查找
                if nums[l] <= nums[mid] and nums[l] <= target <= nums[mid]:
                    r = mid
                # 相似的，对称过来也是一样的
                elif nums[mid] <= nums[r] and nums[mid] <= target <= nums[r]:
                    l = mid
                # 如果左区间是连续的，但是target在右区间，那么这一轮无法转换，缩小范围，下一轮继续逼近
                elif nums[l] <= nums[mid] and (target > nums[mid] or target < nums[l]):
                    l = mid+1
                # 相似的，对称过来也是一样的
                elif nums[mid] <= nums[r] and (target < nums[mid] or target > nums[r]):
                    r = mid-1
                # 如果都不满足，说明不存在
                else:
                    return -1
        return result


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.search(*tc))

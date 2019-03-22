from typing import List
tcs = [
    ([2, 1, 2, 2, 1, 2, 1, 16],),
]


class Solution:

    # 方法1：counter.时间复杂度n,空间复杂度n
    def m1(self, nums):
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]

    # 方法2：排序后中间元素即是
    def m2(self, nums: list):
        nums.sort()
        return nums[int(len(nums)/2)]

    # 方法3：利用大于一半的特点，对计数器进行类似消除的操作。因为量大，所以总能消除掉其他数的计数。
    def find_verbose(self, nums):
        count = 0
        this_num = nums[0]
        for i in nums:
            if i == this_num:
                count += 1
            else:
                count -= 1
            if count < 0:
                this_num = i
            print(i, count)
        return this_num


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.m2(*tc))

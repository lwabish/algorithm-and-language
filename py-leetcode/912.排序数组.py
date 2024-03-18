from typing import List
tcs = [
    ([5, 2, 3, 1],),
    ([1, 1, 1, 1,],),
]


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums
        if n == 2:
            return [nums[0], nums[1]] if nums[0] < nums[1] else [nums[1], nums[0]]

        # leetcode测试用例中有极端数据
        # 随机化p指针可以解决
        # p = int(n/2)
        import random
        p = random.randint(0, n-1)

        smaller = [i for i in nums if i < nums[p]]
        equaller = [i for i in nums if i == nums[p]]
        larger = [i for i in nums if i > nums[p]]
        if not smaller and not larger:
            return equaller
        return self.sortArray(smaller)+self.sortArray(equaller) + self.sortArray(larger)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.sortArray(*tc))

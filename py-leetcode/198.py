from typing import List
tcs = [
    ([2, 7, 9, 3, 1],),
    ([1, 2, 3, 1],),
    ([3],),
    ([1, 2],),
    ([2, 1],),
]


class Solution:
    def rob(self, nums: List[int]) -> int:
        before_1, before_2, this = -1, -1, 0
        for num in nums:
            if before_2 == -1:
                before_2 = num
                this = before_2
                continue
            if before_1 == -1:
                before_1 = max(num, before_2)
                this = before_1
                continue
            this = max(num + before_2, before_1)
            before_2 = before_1
            before_1 = this
        return this


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.rob(*tc))

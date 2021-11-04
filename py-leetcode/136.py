from functools import reduce
from typing import List
tcs = [
    ([4, 1, 2, 1, 2],),
]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        只出现一次的数字
        O(n) O(1)
        基于异或，交换律结合律
        x ^ x = 0
        x ^ 0 = x
        """
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.singleNumber(*tc))

from typing import List
from collections import defaultdict
tcs = [
    ([2, 2, 1, 1, 1, 2, 2],),
]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        数组中的多数元素
        O(n) O(1)
        """
        counts = defaultdict(lambda: 0)
        common_count = 0
        common_value = None
        for i in nums:
            counts[i] += 1
            if counts[i] > common_count:
                common_count = counts[i]
                common_value = i
        return common_value


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.majorityElement(*tc))

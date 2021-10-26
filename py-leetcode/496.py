from typing import List
from collections import defaultdict
tcs = [
    ([4, 1, 2], [1, 3, 4, 2]),
]


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = {}
        for i, v in enumerate(nums1):
            result[v] = -1
            for j, w in enumerate(nums2[nums2.index(v)+1:]):
                if w > v:
                    result[v] = w
                    break
        return list(result.values())


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.nextGreaterElement(*tc))

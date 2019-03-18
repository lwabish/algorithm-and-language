from typing import List
tcs = [
    ([1, 2, 2, 1], [2, 2]),
    ([4, 9, 5], [9, 4, 9, 8, 4]),
]


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = set(nums1) & set(nums2)
        res = []
        for num in nums:
            res += [num] * min(nums1.count(num), nums2.count(num))
        return res


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.intersect(*tc))

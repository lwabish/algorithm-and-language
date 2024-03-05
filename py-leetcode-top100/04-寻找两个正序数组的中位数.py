from typing import List
tcs = [
    ([1, 3, 4, 5, 6, 7], [2]),
    ([1, 2], [3, 4]),
]


# o(log(m+n))的方法研究起来成本较高，跳过。
# 归并排序比较容易实现，但复杂度需要o(m+n)
# todo: 复习归并排序时一起写
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.findMedianSortedArrays(*tc))

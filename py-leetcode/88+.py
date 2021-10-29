from typing import List
tcs = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
]


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        合并有序数组
        重要线索：nums1已经把空位准备好了，所以沿着这个线索，应该从nums1右端沿着空位从大到小改写nums1
        """
        writer = len(nums1)-1
        while m > 0 or n > 0:
            if m > 0 and n > 0:
                if nums1[m - 1] > nums2[n-1]:
                    nums1[writer] = nums1[m-1]
                    m -= 1
                else:
                    nums1[writer] = nums2[n-1]
                    n -= 1
            elif m > 0:
                nums1[writer] = nums1[m-1]
                m -= 1
            elif n > 0:
                nums1[writer] = nums2[n-1]
                n -= 1
            writer -= 1
        return nums1


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.merge(*tc))

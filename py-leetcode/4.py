from typing import List
tcs = [
    ([1, 2], [3, 4]),
    ([], [1, 2]),
    ([0, 2], [1])
]


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        orderedList = self.mergeOrderedLists(nums1, nums2)
        return self.calculateMedian(orderedList)

    def mergeOrderedLists(self, l1: List[int], l2: List[int]):
        result = []
        while l1 or l2:
            if l1 and l2:
                result.append(
                    l2.pop(0)) if l1[0] > l2[0] else result.append(l1.pop(0))
            elif l1:
                result.append(l1.pop(0))
            else:
                result.append(l2.pop(0))
        return result

    def calculateMedian(self, nums: List[int]) -> float:
        if not nums:
            return float(0)
        if len(nums) % 2 == 0:
            index1 = int(len(nums)/2)
            index2 = int(len(nums)/2-1)
            return (nums[index1]+nums[index2])/2.0
        else:
            index = len(nums)//2
            return float(nums[index])


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.findMedianSortedArrays(*tc))

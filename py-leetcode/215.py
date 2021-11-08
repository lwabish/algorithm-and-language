from typing import List
import heapq
tcs = [
    ([3, 2, 1, 5, 6, 4], 2),
]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        result = None
        for _ in range(len(nums)-k+1):
            result = heapq.heappop(nums)
        return result


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.findKthLargest(*tc))

from typing import List
tcs = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 11),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 15),
]


# 思路比较容易想到
# 只要能掌握标准二分和35题，在其基础上写两次二分查找即可
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m-1
        while l <= r:
            mid = int((l+r)/2)
            head = matrix[mid][0]
            if head == target:
                return True
            elif head < target:
                l = mid+1
            else:
                r = mid - 1

        line = matrix[l-1]
        l, r = 0, n-1
        while l <= r:
            mid = int((l+r)/2)
            if line[mid] == target:
                return True
            elif line[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return False


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.searchMatrix(*tc))

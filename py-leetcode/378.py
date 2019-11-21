from typing import List
tcs = [
    ([
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ],),
    ([
        [1]
    ],),
]


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        return matrix[k//n][k % n-1]


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.kthSmallest(*tc, 1))

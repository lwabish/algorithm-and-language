from typing import List
from my_data_structure import print_matrix
tcs = [
    ([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],),
]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for r in range(len(matrix)):
            for c in range(r+1, len(matrix[0])):
                if r != c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            matrix[r] = matrix[r][::-1]


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        solution.rotate(*tc)
        print_matrix(*tc)

from typing import List
from collections import defaultdict
tcs = [
    ([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ],),
    ([
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ],),
]


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        """
        row_hash, column_hash, sub_hash = defaultdict(
            set), defaultdict(set), defaultdict(set)
        for row_id in range(len(board)):
            for c_id in range(len(board[0])):
                sub_id = 3*(row_id//3)+c_id//3+1
                this_value = board[row_id][c_id]
                if this_value == '.':
                    continue
                if this_value in row_hash[row_id] or this_value in column_hash[c_id] or this_value in sub_hash[sub_id]:
                    return False
                else:
                    row_hash[row_id].add(this_value)
                    column_hash[c_id].add(this_value)
                    sub_hash[sub_id].add(this_value)
        return True


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isValidSudoku(*tc))

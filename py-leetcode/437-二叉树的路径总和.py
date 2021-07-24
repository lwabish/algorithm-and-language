from typing import List
from lwabish.algorithm.tree import TreeNode, new_tree
tcs = [
    (new_tree("10,5,-3,3,2,null,11,3,-2,null,1"),),
]


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        pass


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.pathSum(*tc))

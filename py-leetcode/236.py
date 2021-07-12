from typing import List
from lwabish.algorithm.tree import TreeNode, new_tree
tcs = [
    (new_tree('3,5,1,6,2,0,8,null,null,7,4'), 5, 1),
]


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pass


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.lowestCommonAncestor(*tc))

from typing import List
from lwabish.algorithm.tree import new_tree, TreeNode
tcs = [
    (new_tree('1,null,2,3'),),
]


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.preorderTraversal(*tc))

from typing import List
from lwabish.algorithm.tree import TreeNode, new_tree
tcs = [
    (new_tree('1,null,2,3'),),
]


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.inorderTraversal(*tc))

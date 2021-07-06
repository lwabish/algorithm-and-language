from typing import List
from lwabish.algorithm.tree import TreeNode, new_tree, print_tree
tcs = [
    (new_tree("4,2,7,1,3,6,9"),),
]


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = self.invertTree(
            root.right), self.invertTree(root.left)
        return root


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_tree(solution.invertTree(*tc))

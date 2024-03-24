from typing import List, Optional
from lwabish.structs.tree import TreeNode, new_tree, print_tree

tcs = [
    (new_tree("1,2,3,4,5"),),
]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = self.invertTree(
            root.right), self.invertTree(root.left)
        return root


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_tree(solution.invertTree(*tc))

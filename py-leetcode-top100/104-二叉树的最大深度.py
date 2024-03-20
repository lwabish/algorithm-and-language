from typing import List, Optional
from lwabish.structs.tree import TreeNode, new_tree, print_tree
tcs = [
    (new_tree("3,9,20,null,null,15,7"),),
]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # print_tree(root)
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.maxDepth(*tc))

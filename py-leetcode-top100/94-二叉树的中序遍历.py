from typing import List, Optional
from lwabish.structs.tree import TreeNode, new_tree
tcs = [
    (new_tree("1, 2, 3"),),
]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left)+[root.val] + self.inorderTraversal(root.right)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.inorderTraversal(*tc))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_depth(root):
            if not root:
                return 0
            l = get_depth(root.left)
            r = get_depth(root.right)
            if l == -1 or r == -1:
                return -1
            if abs(l-r) > 1:
                return -1
            return max(l, r)+1
        if get_depth(root) == -1:
            return False
        return True

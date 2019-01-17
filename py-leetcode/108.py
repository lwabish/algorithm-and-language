# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        else:
            mid = int(len(nums)/2)
            tn = TreeNode(nums[mid])
            tn.left = self.sortedArrayToBST(nums[:mid])
            tn.right = self.sortedArrayToBST(nums[mid+1:len(nums)])
        return tn

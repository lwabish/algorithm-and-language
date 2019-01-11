def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:  # 不仅可以判断空树，而且可以规避所有递归中的空节点
        return 0
    l = 1 + self.maxDepth(root.left)  # 递归中如果需要对中间结果进行操作，不return，给变量即可
    r = 1 + self.maxDepth(root.right)
    if l > r:
        return l
    else:
        return r

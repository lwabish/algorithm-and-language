def levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    this_floor_tree = [root] if root != None else [
    ]   # 类似于广度优先搜索，每次处理一层后，再加入下一层
    result = []
    while this_floor_tree:
        next_floor_tree = []
        this_floor_value = []
        for i in this_floor_tree:
            if i.left != None:
                next_floor_tree.append(i.left)
            if i.right != None:
                next_floor_tree.append(i.right)
            this_floor_value.append(i.val)
        result.insert(0, this_floor_value)
        this_floor_tree = next_floor_tree

    return result

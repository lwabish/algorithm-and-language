from my_data_structure import generate_treenode, get_specific_treenode, print_treenode

# 给定一颗二叉树和一个节点，找到其中序遍历序列的下一个节点
# 注：该二叉树的节点除了有左右子节点，还有父节点

# 书上的普通二叉树
tc = '1,2,3,4,5,6,7,null,null,8,9'
# 只有左子树的二叉树
tc = '1,2,null,3,null,4,null'
# 只有右子树的二叉树
tc = '1,null,2,null,3,null,4'
# 单节点
tc = '1'


def main(node):
    if node.right:
        node = node.right  # 从右子树开始寻找
        while node.left:  # 一路到底，尝试往左
            node = node.left
        return node.val
    else:
        if not node.parent:  # 无父节点
            return '最后一位'
        if node.parent.left and node.parent.left.val == node.val:  # 是父节点的左子节点
            return node.parent.val
        else:  # 是父节点的右子节点
            while node.parent:  # 沿右子节点路线一路向上到顶
                if node.parent.right.val == node.val:
                    node = node.parent
                else:
                    break
            if node.parent:
                return node.parent.val
            else:
                return '最后一位'


if __name__ == '__main__':
    # 打印出当前测试用例的二叉树形状
    tc_tree = generate_treenode(tc, True)
    print_treenode(tc_tree)

    # 遍历测试每个节点的下一个节点
    t, num = 1, 1   # 将num修改为二叉树中节点的个数
    while t <= num:
        tc_node = get_specific_treenode(tc_tree, t)
        print(tc_node.val, main(tc_node), '\n')
        t += 1

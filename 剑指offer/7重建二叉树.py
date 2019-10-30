# 根据前序遍历和中序遍历，重建出一颗二叉树
from luabish.dsaa import TreeNode, print_treenode, generate_treenode

# 测试用例1：普通二叉树
# 生成目标树
tc_tree = generate_treenode('3,9,20,null,null,15,7')
# 目标树的前序遍历
tc_preorder = [3, 9, 20, 15, 7]
# 目标树的中序遍历
tc_inorder = [9, 3, 15, 20, 7]

# 测试用例2：只有左子节点的二叉树
tc_tree = generate_treenode('3,9,null,2')
# 目标树的前序遍历
tc_preorder = [3, 9, 2]
# 目标树的中序遍历
tc_inorder = [2, 9, 3]

# 测试用例3：只有一个节点
tc_tree = generate_treenode('3')
# 目标树的前序遍历
tc_preorder = [3]
# 目标树的中序遍历
tc_inorder = [3]


def main(preorder, inorder):
    # 从前序遍历找到根节点的值
    this_root = preorder[0]
    # 找到根节点在中序遍历中的索引
    this_root_inorder_index = inorder.index(this_root)

    # 根据根节点的索引，切出中序遍历的左右子树
    left_sub_tree_inorder = inorder[:this_root_inorder_index]
    right_sub_tree_inorder = inorder[this_root_inorder_index + 1:]

    # 根据中序遍历的左右子树，切出左右子树的前序遍历
    left_sub_tree_preorder = preorder[1:len(left_sub_tree_inorder)+1]
    right_sub_tree_preorder = preorder[len(left_sub_tree_inorder) + 1:]
    # print(left_sub_tree_preorder, right_sub_tree_preorder)
    # 基线条件
    if len(left_sub_tree_inorder) < 2 and len(right_sub_tree_inorder) < 2:
        sub_root = TreeNode(this_root)
        if left_sub_tree_inorder:
            sub_root.left = TreeNode(left_sub_tree_inorder[0])
        if right_sub_tree_inorder:
            sub_root.right = TreeNode(right_sub_tree_inorder[0])
        return sub_root
    root = TreeNode(this_root)
    if left_sub_tree_inorder:
        # 将左子树递归分解并拼装
        root.left = main(left_sub_tree_preorder, left_sub_tree_inorder)
    if right_sub_tree_inorder:
        # 将右子树递归分解并拼装
        root.right = main(right_sub_tree_preorder, right_sub_tree_inorder)
    return root
    # print(left_sub_tree, right_sub_tree)


if __name__ == '__main__':
    print_treenode(tc_tree)
    print_treenode(main(tc_preorder, tc_inorder))

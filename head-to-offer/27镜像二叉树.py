from my_data_structure import generate_treenode, print_treenode

tc = [
    generate_treenode('8,6,10,5,7,9,11'),
    # 只有一个节点的二叉树
    generate_treenode('1'),
    # 只有左子树的二叉树
    generate_treenode('1,2,null,4'),
]


def main(tree):
    if tree.left == tree.right == None:
        return tree
    tree.left, tree.right = tree.right, tree.left
    if tree.left:
        main(tree.left)
    if tree.right:
        main(tree.right)
    return tree


if __name__ == '__main__':
    for t in tc:
        print_treenode(main(t))

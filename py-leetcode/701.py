from my_data_structure import generate_treenode, print_treenode, TreeNode
tc = [
    generate_treenode('4,2,7,1,3')
]


def insertIntoBST(root, val: int):
    head = root

    def insert(root, val):
        if root.val > val:
            if root.left:
                insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
    insert(root, val)
    return head


if __name__ == '__main__':
    print_treenode(insertIntoBST(tc[0], 5))

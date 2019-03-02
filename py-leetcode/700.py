from my_data_structure import generate_treenode, print_treenode
tc = [
    generate_treenode('4,2,7,1,3,5,6')
]


def searchBST(root, val: int):
    if not root:
        return None
    if root.val == val:
        return root
    if root.val > val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)


if __name__ == '__main__':
    print_treenode(searchBST(tc[0], 7))

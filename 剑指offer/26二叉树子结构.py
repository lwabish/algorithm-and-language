from my_data_structure import generate_treenode, print_treenode

tc = [
    generate_treenode('8,8,7,9,2,null,null,null,null,4,7'),
    generate_treenode('8,9,2')
]

tc = [
    generate_treenode(str(list(range(1, 16)))[1:-1]),  # 四层满二叉树
    generate_treenode('5,10,1')
]

tc = [
    generate_treenode('1,2,null,4'),
    generate_treenode('2,null,4')
]
tc = [
    generate_treenode('1,2,null,4'),
    generate_treenode('10')
]


def main(root1, root2):

    # 要特别注意传进来none的情况
    def check_if_same(root1, root2):
        # 都为None
        if not root1 and not root2:
            return True
        # 不都为none，但有none，说明一个是none，一个是数字
        if not root1 or not root2:
            return False
        # 两个都不为none
        if root1.val != root2.val:
            return False
        # 到了root2的底，值仍然相等
        if root2.left == root2.right == None:
            return True
        # 递归对左子树和右子树分别判断，结果必须都为true才能返回true
        return check_if_same(root1.left, root2.left) and check_if_same(root1.right, root2.right)

    def find_root(root, value):
        """
        递归找root1中值为root2的节点
        """
        # 空节点
        if not root:
            return None
        # 找到了等于value的节点
        if root.val == value:
            return root
        # 值不相等，且已经到了尾巴
        if not root.left and not root.right:
            return None
        # 递归对左子树进行查找
        l = find_root(root.left, value)
        if l:
            return l
        # 递归对右子树进行查找
        r = find_root(root.right, value)
        if r:
            return r

    maybe_root = find_root(root1, root2.val)
    if maybe_root:
        if check_if_same(maybe_root, root2):
            return True
        else:
            # 对左右子树分别查找，只要有一个找到就返回true
            return main(root1.left, root2) or main(root1.right, root2)
    return False


if __name__ == '__main__':
    print(main(tc[0], tc[1]))

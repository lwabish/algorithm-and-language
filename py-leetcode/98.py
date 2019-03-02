from my_data_structure import generate_treenode, print_treenode

tc = [
    generate_treenode('0,null,-1')
]


def main(root) -> bool:
    def judge(root, down, up):
        if not root:
            return True
        if (down and root.val <= down.val) or (up and root.val >= up.val):
            return False
        return judge(root.left, down, root) and judge(root.right, root, up)
    return judge(root, None, None)


def main1(root) -> bool:
    def judge(root, down, up):
        if not root:
            return True
        if (down > -float('inf') and root.val <= down) or (up < float('inf') and root.val >= up):
            return False
        return judge(root.left, down, root.val) and judge(root.right, root.val, up)
    return judge(root, -float('inf'), float('inf'))


if __name__ == '__main__':
    for i in tc:
        print(main1(i))

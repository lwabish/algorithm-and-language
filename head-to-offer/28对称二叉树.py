# leetcode101
# 此处用书上思路实现：对比前序遍历和前序遍历的对称遍历结果
from my_data_structure import generate_treenode, print_treenode

tc = [
    # 对称二叉树
    generate_treenode('8,6,6,5,7,7,5'),
    # 结构对称，值不对称
    generate_treenode('8,6,9,5,7,7,5'),
    # 结构不对称
    generate_treenode('7,7,7,7,7,7'),
    # 只有左子节点的二叉树
    generate_treenode('1,2,null,4'),
    # 单节点二叉树
    generate_treenode('1'),
]


def main(tree):
    pre = list()
    pre_reversed = list()

    # 前序遍历，结果存储在pre列表里
    def preoder_traverse(tree):
        if not tree:
            pre.append('null')
            return
        if tree.left == tree.right == None:
            pre.append(tree.val)
            return
        pre.append(tree.val)
        preoder_traverse(tree.left)
        preoder_traverse(tree.right)
    # 前序遍历中把左右顺序颠倒：根右左。结果存储在pre_reversed列表里

    def preoder_reverse_traverse(tree):
        if not tree:
            pre_reversed.append('null')
            return
        if tree.left == tree.right == None:
            pre_reversed.append(tree.val)
            return
        pre_reversed.append(tree.val)
        preoder_reverse_traverse(tree.right)
        preoder_reverse_traverse(tree.left)
    preoder_traverse(tree)
    preoder_reverse_traverse(tree)
    # print(pre, pre_reversed)
    # print(pre == pre_reversed)
    return pre == pre_reversed


if __name__ == '__main__':
    for i in tc:
        print(main(i))

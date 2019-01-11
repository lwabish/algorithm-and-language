# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def main(p, q):
    def tree_to_list(t):
        '''
        转换准则：子树左侧空，右侧不空，则标记空元素一个
        思路类似于逆序数，正常不管，只标记处树中不按从左到右排序的即可唯一表示一棵树
        '''
        from collections import deque
        line = deque()
        if t != None:
            line.append(t)
        l = list()
        while line:
            head = line.popleft()
            if type(head) != str:
                l.append(head.val)
                if head.left:
                    if head.right:
                        line.append(head.left)
                        line.append(head.right)
                    else:
                        line.append(head.left)
                elif head.right:
                    line.append('')
                    line.append(head.right)
            else:
                l.append(head)
        return l
    tree_l1 = tree_to_list(p)
    tree_l2 = tree_to_list(q)
    # print(tree_l1, tree_l2)
    if tree_l1 != tree_l2:
        return False
    else:
        return True

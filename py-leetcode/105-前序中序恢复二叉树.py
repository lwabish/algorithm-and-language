from typing import List
from lwabish.algorithm.tree import TreeNode, print_tree, new_tree
tcs = [
    ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
    ([1, 3, 4], [1, 3, 4])
]


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 有可能切出[]
        if not preorder:
            return None
        # 最小有效list
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        # 前序提供根：第一个元素
        root_val = preorder[0]
        # 中序提供左右子树的结构
        root_val_index_mid = inorder.index(root_val)

        # 前序中序长度一定一样，按照根元素和左右子树结构，进行切分
        mid_left = inorder[:root_val_index_mid]
        mid_right = inorder[root_val_index_mid+1:]
        pre_left = preorder[1:len(mid_left)+1]
        pre_right = preorder[1+len(mid_left):]

        root = TreeNode(root_val)

        # 递归组装
        root.left = self.buildTree(pre_left, mid_left)
        root.right = self.buildTree(pre_right, mid_right)

        return root


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_tree(solution.buildTree(*tc))

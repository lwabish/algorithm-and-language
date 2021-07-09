from typing import List
from lwabish.algorithm.tree import TreeNode, new_tree, print_tree
tcs = [
    (new_tree('1,2,5,3,4,null,6'),),
    (new_tree('1,null,2'),),
    (new_tree('1,null,2,3'),),
]


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        def attach_to_leaf(root1, root2):
            """
            把root2拼接到root1的尾巴上
            """
            if not root1:
                return None
            if not root1.right:
                root1.right = root2
            else:
                attach_to_leaf(root1.right, root2)

        # 对右子树进行深度优先遍历，展平
        flattened_right = self.flatten(root.right)
        # 对左子树进行深度优先遍历，展平
        flattened_left = self.flatten(root.left)

        root.left, root.right = None, flattened_left

        # 把暂存的原来的右子树安到右边的叶子上
        attach_to_leaf(root, flattened_right)

        return root


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_tree(solution.flatten(*tc))

from typing import List
from lwabish.algorithm.tree import TreeNode, new_tree, print_tree
tcs = [
    (new_tree("1,2,3,4,5"),),
    (new_tree("4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2"),)
]


class Solution:
    """
    官方题解方案
    技巧：遍历时更新全局变量
    """

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.d = 0

        def depth(root: TreeNode):
            if not root:
                return 0
            l = depth(root.left)
            r = depth(root.right)

            # 更新全局最大值
            self.d = max(l+r, self.d)

            return max(l, r)+1

        depth(root)
        return self.d


class Solution1:
    """
    版本1：遍历所有子树，求每个节点左右子树的深度加和，最大值即为所求
    效率比较低下
    """

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def maxDepth(root: TreeNode, n):
            """
            求二叉树最大深度
            """
            if not root:
                return n-1
            return max(maxDepth(root.left, n+1), maxDepth(root.right, n+1))

        if not root:
            return 0
        return max(maxDepth(root.left, 1)+maxDepth(root.right, 1), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_tree(*tc)
        print(solution.diameterOfBinaryTree(*tc))

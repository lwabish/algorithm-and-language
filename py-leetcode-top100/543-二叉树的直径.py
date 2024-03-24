from typing import List, Optional
from lwabish.structs.tree import TreeNode, new_tree
tcs = [
    (new_tree("1,2,3,4,5,6"),),
]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 在算深度的同时，更新最大节点数
# 理解深度与节点数的区别
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 最大节点数量
        self.res = 1

        # 函数本身：算深度
        def depth(root: TreeNode):
            if not root:
                return 0
            L = depth(root.left)
            R = depth(root.right)
            # 重难点：更新最大节点数
            self.res = max(self.res, L+R+1)
            return max(L, R)+1

        depth(root)

        # 结果是节点数量-1=边的数量
        return self.res - 1


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.diameterOfBinaryTree(*tc))

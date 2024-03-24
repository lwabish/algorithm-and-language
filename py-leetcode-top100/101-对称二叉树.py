from typing import List, Optional
from lwabish.structs.tree import TreeNode, new_tree
tcs = [
    (new_tree("1,2,2,3,4,5,6"),),
    (new_tree("1,2,2,2,2,2,2"),),
]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 关键：递归时进入同一函数栈的两个根节点不是同一个，而是轴对称的两个
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def judge(left: TreeNode, right: TreeNode):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and judge(left.right, right.left) and judge(left.left, right.right)

        return judge(root.left, root.right)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isSymmetric(*tc))

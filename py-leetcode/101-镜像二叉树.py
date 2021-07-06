from typing import List
from lwabish.algorithm.tree import TreeNode, new_tree
tcs = [
    (new_tree("3, 9, 20, null, null, 15, 7"),),
]


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def check(left: TreeNode, right: TreeNode):
            if not left and not right:
                return True
            # 这个if里本有三种情况，但是有一种在上面已经return了
            if not left or not right:
                return False
            return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)
        if not root:
            return True
        return check(root.left, root.right)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isSymmetric(*tc))

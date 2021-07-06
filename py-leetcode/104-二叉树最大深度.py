from typing import List
from lwabish.algorithm.tree import TreeNode, new_tree
tcs = [
    (new_tree("3,9,20,null,null,15,7"),),
]


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def count(root: TreeNode, n):
            if not root:
                return n-1
            return max(count(root.left, n+1), count(root.right, n+1))

        if not root:
            return 0
        return count(root, 1)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.maxDepth(*tc))

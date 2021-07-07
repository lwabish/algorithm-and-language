from typing import List, NewType
from lwabish.algorithm.tree import TreeNode, new_tree, print_tree
tcs = [
    (new_tree("1,3,2,5"), new_tree("2,1,3,null,4,null,7")),
]


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return None
        if not root1 and root2:
            return root2
        if not root2 and root1:
            return root1

        merged = TreeNode(root1.val+root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_tree(tc[0])
        print_tree(tc[1])
        print_tree(solution.mergeTrees(*tc))

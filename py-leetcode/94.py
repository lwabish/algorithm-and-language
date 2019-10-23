from typing import List
from luabish.dsaa import generate_treenode, TreeNode
tcs = [
    (generate_treenode('1,null,2,3'),),
]


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        if root.left == root.right == None:
            return [root.val]
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.inorderTraversal(*tc))

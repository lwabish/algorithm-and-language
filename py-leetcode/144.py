from typing import List
from luabish.dsaa import TreeNode, generate_treenode
tcs = [
    (generate_treenode('1,null,2,3'),),
]


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        if root.left == root.right == None:
            return [root.val]
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.preorderTraversal(*tc))

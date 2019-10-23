from typing import List
from luabish.dsaa import generate_treenode, TreeNode
tcs = [
    (generate_treenode('1,null,2,3'),),
]


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        if root.left == root.right == None:
            return [root.val]
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.postorderTraversal(*tc))

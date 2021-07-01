from typing import List
from lwabish.algorithm.tree import TreeNode, new_tree
tcs = [
    (new_tree('1,null,2,3'),),
]


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        # 左右中
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.postorderTraversal(*tc))

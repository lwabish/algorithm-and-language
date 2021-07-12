from typing import List
from lwabish.algorithm.tree import TreeNode, new_tree
tcs = [
    (new_tree('3,5,1,6,2,0,8,null,null,7,4'), 5, 1),
]


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 递归终止
        if not root or root.val == p.val or root.val == q.val:
            return root

        # dfs递归
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, q, p)

        # 四种情况return不同值
        if not l and not r:
            return None
        if not l:
            return r
        if not r:
            return l
        return root


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.lowestCommonAncestor(*tc))

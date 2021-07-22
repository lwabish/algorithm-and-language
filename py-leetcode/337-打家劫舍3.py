from typing import List
from lwabish.algorithm.tree import TreeNode, new_tree
tcs = [
    (new_tree("3,2,3,null,3,null,1"),),
]


class Solution:
    def rob(self, root: TreeNode) -> int:
        cache = {}

        def cache_or_cal(root: TreeNode):
            result = cache.get(root, None)
            if result:
                return result
            else:
                result = do_rob(root)
                cache[root] = result
                return result

        def do_rob(root: TreeNode):
            if not root:
                return 0
            sons = cache_or_cal(root.left) + cache_or_cal(root.right)
            grand_sons = 0
            if root.left:
                grand_sons += cache_or_cal(root.left.left) + \
                    cache_or_cal(root.left.right)
            if root.right:
                grand_sons += cache_or_cal(root.right.left) + \
                    cache_or_cal(root.right.right)
            return max(root.val+grand_sons, sons)
        return do_rob(root)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.rob(*tc))

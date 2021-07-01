from typing import List
from lwabish.algorithm.tree import TreeNode, new_tree
tcs = [
    (new_tree(
        ','.join(map(lambda x:str(x), [3, 9, 20, 'null', 'null', 15, 7]))),),
]


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = list()
        if not root:
            return res

        def go(root: TreeNode, level):
            """
            leve:索引
            """
            if len(res) < level + 1:
                res.append(list())
            res[level].append(root.val)
            if root.left:
                go(root.left, level + 1)
            if root.right:
                go(root.right, level+1)
        go(root, 0)
        return res


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.levelOrder(*tc))

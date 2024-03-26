from typing import List, Optional
from lwabish.structs.tree import TreeNode, new_tree

tcs = [
    (new_tree("1,2,3,4,5,6"),),
]


# 和普通广度优先遍历稍有区别，一次取多个
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q, n = [root], 1
        result = []

        while q:
            nodes = [q.pop(0) for i in range(n)]
            result.append(list(map(lambda x: x.val, nodes)))
            n = 0
            for node in nodes:
                if node.left:
                    q.append(node.left)
                    n += 1
                if node.right:
                    q.append(node.right)
                    n += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.levelOrder(*tc))

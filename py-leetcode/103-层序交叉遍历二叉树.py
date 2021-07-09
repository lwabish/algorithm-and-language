from typing import List
from lwabish.algorithm.tree import TreeNode, new_tree
from collections import deque
tcs = [
    (new_tree('3, 9, 20, null, null, 15, 7'),)
]


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        result = []
        # 在普通的层序遍历基础上，增加一个开关表示是否反转即可
        reverse = False
        while q:
            this_level_nodes = []
            for i in range(len(q)):
                node = q.popleft()
                this_level_nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if reverse:
                this_level_nodes.reverse()
            result.append(this_level_nodes)
            reverse = not reverse
        return result


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.zigzagLevelOrder(*tc))

from typing import List
from lwabish.algorithm.tree import TreeNode, new_tree
tcs = [
    (new_tree(','.join(map(lambda x:str(x),
     [3, 9, 20, 'null', 'null', 15, 7]))),),
    (new_tree(','.join(map(lambda x:str(x),
     [1, 2, 'null', 3, 'null', 4, 'null', 5, ]))),)
]


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = [root]
        level = 0

        result = []

        while q:
            # 初始化result里每层的list
            if len(result) < level+1:
                result.append([])

            # while循环每次开始时，q里放的是本层所有的tree node，所以循环len(q)次即可批量处理一层
            for i in range(len(q)):

                node = q.pop(0)

                result[level].append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.levelOrder(*tc))

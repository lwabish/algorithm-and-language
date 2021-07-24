import time
from typing import List, NewType
from lwabish.algorithm.tree import TreeNode, new_tree, print_tree
tcs = [
    (new_tree("-10,9,20,null,null,15,7"),),
    (new_tree("9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6"),)
]


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = root.val

        def do(root: TreeNode):
            if not root:
                return 0
            # 1. 计算每个节点的贡献值：空节点0，叶节点val，非叶节点val+max(左右)
            l = do(root.left)
            r = do(root.right)
            value = root.val+(max(l, r)if max(l, r) > 0 else 0)
            # 2. 用贡献值计算节点的路径和，更新全局变量：val+左贡献+右贡献（仅正贡献）
            tmp = root.val+(l if l > 0 else 0) + (r if r > 0 else 0)
            print(root.val, l, r, tmp)
            if tmp > self.max_sum:
                self.max_sum = tmp
            return value

        do(root)
        return self.max_sum


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_tree(*tc)
        print(solution.maxPathSum(*tc))

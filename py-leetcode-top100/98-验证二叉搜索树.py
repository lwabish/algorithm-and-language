from typing import List, Optional
from lwabish.structs.tree import TreeNode, new_tree


tcs = [
    (new_tree("5,4,6,null,null,3,7"),),
    (new_tree("1,null,1"),)
]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 面试时遇到了这个题，面试前恰好尝试过，但是实现有问题，最后看了一眼题解有别的事就搁置了
# 没想到面试遇到了。当时想到了中序遍历的方法，然后写了。面试官要求再用递归写
# 最后经过一些小的debug，最后甚至还用测试用例跑了测了一下没问题
# 最后在leetcode试了下竟然没问题（通常面试中大脑只能发挥出50-70%的脑力，这次面试体验不一般，感觉大脑比较正常）
# 面试官也很给力，没有压迫感，且在一起debug的过程中指出了关键问题
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.judge(float("-inf"), float("inf"), root)

    def judge(self, l, r, node):
        if not node:
            return True
        if node.val >= r or node.val <= l:
            return False
        return self.judge(l, node.val, node.left) and self.judge(node.val, r, node.right)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isValidBST(*tc))

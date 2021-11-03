from typing import List
from lwabish.structureutils.listnode import *
tcs = [
    (get_first_node_by_value(new_listnode(list(range(10))), 5),),
]


class Solution:
    def deleteNode(self, node):
        """
        删除某节点
        删除时带引号的
        关键条件：待删除的节点不是tail
        可以把自己仿冒成下一个node，然后删掉下一个node
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.deleteNode(*tc))

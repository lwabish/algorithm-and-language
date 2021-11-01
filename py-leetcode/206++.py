from typing import List
from lwabish.structureutils.listnode import *
tcs = [
    (new_listnode([1, 2, 3]),),
    (new_listnode([1]),),
    (new_listnode([]),),
]


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归版本
        """
        if not head:
            return head
        return self.doReverse(head, None)

    def doReverse(self, this: ListNode, parent: ListNode):
        next_node = this.next
        this.next = parent
        if next_node is None:
            # 递归终止
            return this
        else:
            return self.doReverse(next_node, this)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.reverseList(*tc))

from typing import List
from lwabish.structureutils.listnode import *
tcs = [
    (new_listnode([1, 2, 4]), new_listnode([1, 3, 4])),
    (new_listnode([]), new_listnode([1])),
    (new_listnode([]), new_listnode([])),
]


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        合并有序链表
        递归版本
        """
        # 递归终止
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.mergeTwoLists(*tc))

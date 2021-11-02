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
        迭代，但是不为结果申请新的空间，原地合并
        """
        if not l1:
            return l2
        elif not l2:
            return l1

        head = ListNode()
        prev = head
        while l1 or l2:
            if not l1:
                prev.next = l2
                break
            elif not l2:
                prev.next = l1
                break
            elif l1.val < l2.val:
                prev.next = l1
                prev = l1
                l1 = l1.next
            else:
                prev.next = l2
                prev = l2
                l2 = l2.next

        return head.next


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.mergeTwoLists(*tc))

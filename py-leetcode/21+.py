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
        只有操作，没有技巧版本
        对result全部申请了新的空间，空间复杂度高，不用关心旧链表的指针
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        # 技巧：dummy head
        # 第一个节点就可以和其他节点共用一样的逻辑
        head = ListNode()
        tail = head
        while l1 or l2:
            this_node = ListNode()
            if not l1:
                this_node.val = l2.val
                l2 = l2.next
            elif not l2:
                this_node.val = l1.val
                l1 = l1.next
            elif l1.val > l2.val:
                this_node.val = l2.val
                l2 = l2.next
            else:
                this_node.val = l1.val
                l1 = l1.next
            tail.next = this_node
            tail = tail.next
        return head.next


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.mergeTwoLists(*tc))

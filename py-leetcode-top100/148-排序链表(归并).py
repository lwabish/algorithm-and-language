from typing import List, Optional
from lwabish.structs.listnode import ListNode, new_listnode, print_listnode
tcs = [
    (new_listnode([-1, 3, 2, 5, 10, 0]),),
]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        other_head, slow.next = slow.next, None
        half1, half2 = self.sortList(head), self.sortList(other_head)
        return self.merge(half1, half2)

    def merge(self, l1: ListNode, l2: ListNode):
        dummy = ListNode(0)
        tail = dummy
        while l1 or l2:
            if l1 and l2:
                next = l1 if l1.val < l2.val else l2
                if next == l1:
                    l1 = l1.next
                else:
                    l2 = l2.next
            elif l1:
                next = l1
                l1 = l1.next
            elif l2:
                next = l2
                l2 = l2.next
            tail.next = next
            tail = tail.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.sortList(*tc))

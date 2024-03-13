from typing import List, Optional
from lwabish.structs.listnode import ListNode, new_listnode, print_listnode
tcs = [
    (new_listnode([1, 2, 4]), new_listnode([0, 3, 6])),
]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        fakeHead = ListNode(-1)
        curTail = fakeHead
        while p1 and p2:
            curTail.next = p1 if p1.val < p2.val else p2
            if p1.val < p2.val:
                p1 = p1.next
            else:
                p2 = p2.next
            curTail = curTail.next
        curTail.next = p1 if p1 else p2
        return fakeHead.next


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.mergeTwoLists(*tc))

from typing import List, Optional
from lwabish.structs.listnode import ListNode, new_listnode, print_listnode
tcs = [
    (new_listnode([9, 9, 9]), new_listnode([1])),
    (new_listnode([3, 4, 2]), new_listnode([4, 6, 5]))
]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        overhead = 0
        fakeHead = ListNode(-1)
        tail = fakeHead
        while l1 or l2:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            total += overhead
            overhead = total // 10
            total = total % 10
            tail.next = ListNode(total)
            tail = tail.next
        # 如果最后还有进位，要单独加一位
        if overhead:
            tail.next = ListNode(overhead)
        return fakeHead.next


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.addTwoNumbers(*tc))

from typing import List, Optional
from lwabish.structs.listnode import ListNode, print_listnode, new_listnode
tcs = [
    (new_listnode([1, 2, 3, 4]), 1),
    (new_listnode([1, 2, 3, 4]), 4),
    (new_listnode([1]), 1),

]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 链表三板斧：哑结点，栈，快慢指针
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        stack = []
        while head:
            stack.append(head)
            head = head.next
        for i in range(n):
            stack.pop()
        target = stack[len(stack)-1] if stack else dummy
        target.next = target.next.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.removeNthFromEnd(*tc))

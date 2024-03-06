from typing import Optional
from lwabish.structs.listnode import ListNode

tcs = [
    (),
]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 快慢指针理论：速度不同，有环时一定能相遇，所以起点无所谓
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        s, f = head, head.next
        while f and f.next and s is not f:
            f = f.next.next
            s = s.next
        if not f or not f.next:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.hasCycle(*tc))

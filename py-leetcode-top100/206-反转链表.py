from typing import Optional
from lwabish.structs.listnode import ListNode, new_random_listnode, print_listnode
tcs = [
    (new_random_listnode(5, 100),),
]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 迭代：梳理清楚每次断谁，接谁，什么顺序
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p, tail = head, None
        while p is not None:
            tmp = p.next
            p.next = tail
            tail = p
            p = tmp
        return tail


# 递归：不易想到
# 使用递归的特性，一直来到尾部
class Solution_Recursion:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead


if __name__ == '__main__':
    solution = Solution_Recursion()
    for tc in tcs:
        print_listnode(*tc)
        print(solution.reverseList(*tc))

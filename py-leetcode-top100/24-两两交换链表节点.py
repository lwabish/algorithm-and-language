from typing import List, Optional
from lwabish.structs.listnode import ListNode, new_listnode, print_listnode
tcs = [
    (new_listnode([1, 2, 3, 4, 5]),),
    (new_listnode([1]),),
    (new_listnode([1, 2, 3, 4]),),
]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 受19题思路启发，类似的思路
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        a, b = [], []
        toA = True
        while head:
            if toA:
                a.append(head)
            else:
                b.append(head)
            head = head.next
            toA = False if toA else True

        fromA = False
        tail = dummy
        while a or b:
            # 奇数情况下特殊处理
            if a and not b:
                tail.next = a.pop(0)
            elif fromA and a:
                tail.next = a.pop(0)
            elif not fromA and b:
                tail.next = b.pop(0)
            tail = tail.next
            fromA = False if fromA else True
        # 偶数情况下尾巴会有环，需要移除掉尾巴的指针
        tail.next = None
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.swapPairs(*tc))

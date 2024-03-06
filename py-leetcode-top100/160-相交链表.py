from typing import List, Optional
from lwabish.structs.listnode import ListNode, new_listnode
tcs = [
    (new_listnode([1, 2, 3, 4, 5]), new_listnode([7, 8, 9])),
]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 朴素且简单的方法：用map存一个链表的节点，遍历另一个链表时查，确定是否有重复的
# 本次实现巧妙的方法
# 思路和实现都不太容易想到
# 思路：消除长度差，然后一同遍历，相交则必会出现两个指针指向同一个节点，否则一起变成None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB
        while pA is not pB:
            # 实现的难点：如何在一次遍历中消除链表的长度差：每个链表走到头后给丫放到另一个链表头。两次即可让二者在同一起跑线
            if pA is None:
                pA = headB
            else:
                pA = pA.next
            if pB is None:
                pB = headA
            else:
                pB = pB.next
        return pA


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.getIntersectionNode(*tc))

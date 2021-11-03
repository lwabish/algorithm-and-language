from typing import List
from lwabish.structureutils.listnode import *

ln1 = new_listnode(list(range(10)))
tcs = [
    (ln1, link_two_listnode(new_listnode(
        list(range(10, 12))), get_first_node_by_value(ln1, 5))),
]


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        判断链表是否相交
        哈希法：过于简单
        双指针数学推导法：过于难想
        折中：长度统一后简单双指针
        """
        # print_listnode(headA)
        # print_listnode(headB)
        if not headA or not headB:
            return None
        # 统计数量
        l1, l2 = 0, 0
        node1, node2 = headA, headB
        while node1:
            node1 = node1.next
            l1 += 1
        while node2:
            node2 = node2.next
            l2 += 1

        # 让长的先走多余的，对齐
        longer = headA if l1 > l2 else headB
        shorter = headB if l1 > l2 else headA
        counter = 0
        while counter < abs(l1-l2):
            longer = longer.next
            counter += 1

        # 一起走，遇到相同的就说明撞了
        while shorter:
            if shorter == longer:
                return shorter
            shorter, longer = shorter.next, longer.next
        return None


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.getIntersectionNode(*tc))

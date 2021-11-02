from typing import List
from lwabish.structureutils.listnode import *
tcs = [
    (
        new_listnode([1, 2, 3, 4]),
        new_listnode([2, 4, 5, 6])
    ),
]


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        合并排序链表
        2019年第一次版本
        """
        if l1 and l2:
            if l1.val < l2.val:
                new_head = l1
                l1 = l1.next
            else:
                new_head = l2
                l2 = l2.next
            current = new_head
        elif l1:
            return l1
        elif l2:
            return l2
        else:
            return None
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
            elif l1:
                current.next = l1
                l1 = l1.next
            elif l2:
                current.next = l2
                l2 = l2.next
            current = current.next
        return new_head


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.mergeTwoLists(*tc))

from typing import List
from lwabish.structureutils.listnode import *

tcs = [
    (add_circle_for_listnode(new_listnode([1, 2, 3, 4, 5, 6]), 3),),
    (new_listnode([1, 2, 3, 4]),),
]


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        判断链表是否有环
        双指针
        朴素版本
        """
        p1, p2 = head, head
        first_flag = True
        while p2:
            if p1 == p2 and first_flag:
                first_flag = False
            elif p1 == p2 and not first_flag:
                return True
            p1 = p1.next
            if not p2.next:
                p2 = p2.next
            else:
                p2 = p2.next.next
        return False


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.hasCycle(*tc))

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
        题解版本
        """
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while slow != fast:
            # 如果没环，快指针将先走到尾巴且无法继续前进，此时该return了
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        # 如果走出了循环，说明slow=fast相遇了，有环
        return True


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.hasCycle(*tc))

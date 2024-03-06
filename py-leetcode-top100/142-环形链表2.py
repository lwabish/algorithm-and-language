from typing import Optional
from lwabish.structs.listnode import ListNode, new_listnode, add_circle_for_listnode


def add_circle(ln):
    return add_circle_for_listnode(ln, 3)


tcs = list(map(add_circle, [new_listnode([1, 2, 3, 4, 5])]))


# 记住数学关系：从头结点出发的快慢指针，在有环的情况相遇后，慢指针和一个新的从头结点出发的指针会在入环点相遇
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        s, f = head, head
        while True:
            if not f.next or not f.next.next:
                return None
            f = f.next.next
            s = s.next
            if s is f:
                p = head
                while p is not s:
                    p = p.next
                    s = s.next
                return p


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.detectCycle(tc))

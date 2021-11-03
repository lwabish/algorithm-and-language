from typing import List
from lwabish.structureutils.listnode import *
tcs = [
    (add_circle_for_listnode(new_listnode([1, 2, 3, 4, 5, 6]), 3),),
    (new_listnode([1, 2, 3, 4]),),
]


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        判断链表是否有环并返回环的入口点
        判断有环同141，注意：141中起始两指针的位置不影响判断，这里要求起始都在head
        环的入口用哈希法容易想，双指针需要数学推导数量关系：
        a为入环前长度，b为环长，n为某整数
        数学推导可以知道，双指针相遇时慢指针走了nb，再走a长度，可以到入口。恰好此时从head到入口也是a。
        因此再次双指针相遇时，即为入口
        https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
        """
        if not head or not head.next:
            return False
        slow, fast = head, head
        while True:
            if not fast or not fast.next:
                return None
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break

        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return fast


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.detectCycle(*tc))

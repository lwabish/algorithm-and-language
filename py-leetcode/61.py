from typing import List, Optional
from lwabish.structureutils.listnode import *
tcs = [
    (new_listnode([1, 2, 3, 4, 5]), 10),
    (new_listnode([1]), 0),
    (new_listnode([1, 2]), 0),
]


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        旋转链表
        问题点：k可能非常大，超过链表长度
        朴素的思路：先遍历一遍，拿到长度。然后k = k % n。
        然后找切断点，重新链接链表，返回新的链表头
        """
        # 空链表、单节点链表、旋转0次的结果都是自己
        if not head or head.next == None or k == 0:
            return head

        # 先拿到链表长度
        current = head
        n = 0
        while current:
            n += 1
            current = current.next

        # 重置指针
        current = head
        result = None
        counter = 1
        k = k % n
        # 如果旋转次数是长度的整数倍，相当于不转，直接返回
        if k == 0:
            return head
        while current:
            # 遍历到了断点
            if counter == n-k:
                result = current.next
                new_tail = current
            # 遍历到了尾巴节点
            if current.next == None:
                current.next = head
                new_tail.next = None
                break
            counter += 1
            current = current.next

        return result


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.rotateRight(*tc))

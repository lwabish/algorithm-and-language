from typing import List
from lwabish.structureutils.listnode import *
tcs = [
    (new_listnode([2, 4, 1, 2, 6, 7, 10, 7]),),
]


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        排序链表
        容易想到的：转成list，排序后再构造新的链表，但是不专业
        递归分治法
        """

        def _sort(head: ListNode, tail: ListNode) -> ListNode:
            # 递归终止
            if not head:
                return None
            # 单节点，原样返回
            if head.next == tail:
                head.next = None
                return head

            # 找中点
            # 特殊之处是，保证fast停在tail上
            slow = fast = head
            while fast != tail:
                fast = fast.next
                slow = slow.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return _merge(_sort(head, mid), _sort(mid, fast))

        def _merge(head1: ListNode, head2: ListNode) -> ListNode:
            """
            参见LeetCode21：合并两个有序链表
            这里直接拿来用即可
            """
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next
        return _sort(head, None)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.sortList(*tc))

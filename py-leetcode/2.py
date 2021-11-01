from typing import List
from lwabish.structureutils.listnode import *
tcs = [
    (new_listnode([2, 4, 3]), new_listnode([5, 6, 4])),
    (new_listnode([0]), new_listnode([0])),

]


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.result = 0
        self.accumulate_listnode(l1)
        self.accumulate_listnode(l2)
        return self.assemble_listnode(str(self.result)[::-1])

    def accumulate_listnode(self, l: ListNode):
        digit = 0
        while l:
            self.result += l.val*pow(10, digit)
            digit += 1
            l = l.next

    def assemble_listnode(self, n: str):
        head = None
        tail = None
        for i, v in enumerate(n):
            if head is None:
                head = ListNode(int(v))
                tail = head
                continue
            # 错误写法：tail.next一开始是none，要新的结果，必须先更新完再引用
            # 用旧值才用交换表达式
            # tail.next, tail = ListNode(int(v)), tail.next
            tail.next = ListNode(int(v))
            tail = tail.next
        return head


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.addTwoNumbers(*tc))

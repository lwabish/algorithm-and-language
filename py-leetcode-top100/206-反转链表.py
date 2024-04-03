from typing import Optional
from lwabish.structs.listnode import ListNode, new_random_listnode, print_listnode
tcs = [
    (new_random_listnode(5, 100),),
]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 迭代：梳理清楚每次断谁，接谁，什么顺序
# 在面试中总犯错误：一次循环总想搞三个节点
# 切记：一次迭代只关注两个节点
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p, tail = head, None
        while p:
            # 缓存下一个节点，因为断链会丢掉
            tmp = p.next
            # 核心操作：断链重接
            p.next = tail
            # 更新尾巴
            tail = p
            # 更新下一个操作对象
            p = tmp
        return tail


# 递归：不易想到
# 使用递归的特性，一直来到尾部
class Solution_Recursion:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead


if __name__ == '__main__':
    solution = Solution_Recursion()
    for tc in tcs:
        print_listnode(*tc)
        print(solution.reverseList(*tc))

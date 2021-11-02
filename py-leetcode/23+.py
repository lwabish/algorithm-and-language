from queue import PriorityQueue
from typing import List
from lwabish.structureutils.listnode import *
tcs = [
    (list(map(new_listnode, [[1, 4, 5], [1, 3, 4], [2, 6]])),),
]


class Solution:
    class ListNodeComparable:
        """
        定义一个内部类，包裹ListNode
        实现__lt__方法以支持优先级队列的比较操作符
        """

        def __init__(self, node: ListNode) -> None:
            self.node = node

        def __lt__(self, other) -> bool:
            return self.node.val < other.node.val

        def __gt__(self, other) -> bool:
            return self.node.val > other.node.val

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        合并排序链表数组
        基于上个版本，用优先级队列优化heads
        """
        # 初始化一个优先级队列，把非空的链表节点头放进去
        heads = PriorityQueue()
        for listnode in lists:
            if listnode:
                heads.put(self.ListNodeComparable(listnode))

        # 初始化result的头和尾
        result_head = ListNode()
        tail = result_head

        while not heads.empty():
            # 从优先级队列heads，拿到最小值
            tail.next = heads.get().node
            # 更新优先级队列
            if tail.next.next:
                heads.put(self.ListNodeComparable(tail.next.next))
            # 更新tail指针
            tail = tail.next
        return result_head.next


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.mergeKLists(*tc))

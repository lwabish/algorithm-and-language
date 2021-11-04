from typing import List
from lwabish.structureutils.listnode import ListNode, new_listnode, print_listnode
tcs = [
    (new_listnode([7, 9, 3, 4, 1]),),
    (new_listnode([2, 2, 1, 1, 3]),),
    (new_listnode([1]),),
    (new_listnode([]),),
]


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        链表插入排序
        自己写的超慢版
        """
        if not head:
            return head
        target = head.next
        prev = head
        while target:
            # 先把target以前断开，方便内层遍历的时候做终止条件
            prev.next = None
            # 备份target的next，以备最后复原
            target_next = target.next

            # 从head到prev遍历，找到target合适的插入点
            insert_point = None
            insert_node = head
            insert_tail = None
            while insert_node:
                if target.val > insert_node.val:
                    insert_point = insert_node
                if not insert_node.next:
                    insert_tail = insert_node
                insert_node = insert_node.next
            # 特殊情况：target的值是最小的，遍历一圈发现得插到头部
            if insert_point is None:
                target.next = head
                head = target
            # 特殊情况，target的值是最大的，插到尾部
            elif insert_point == insert_tail:
                insert_tail.next = target
                insert_tail = target
            # 其他情况插到中间
            else:
                insert_point_next = insert_point.next
                insert_point.next = target
                target.next = insert_point_next

            # 重新连上
            insert_tail.next = target_next
            prev = insert_tail
            target = target_next

        return head


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.insertionSortList(*tc))

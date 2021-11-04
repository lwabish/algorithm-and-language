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
        题解优化版
        """
        if not head:
            return head

        dummy_head = ListNode()
        dummy_head.next = head

        target = head.next
        sorted_tail = head

        while target:
            if target.val >= sorted_tail.val:
                sorted_tail = sorted_tail.next
            else:
                # 隐含逻辑：如果target不比已排序的末尾大，那么在前面肯定能找到插入点
                insert_point = dummy_head
                while insert_point.next.val <= target.val:
                    # 插入点不断前移，直到遇到insert_point的下一个node比targe大了，此时就可以把
                    # target插入到insert_point后面了
                    insert_point = insert_point.next

                # 如何调整链表的node位置
                # 1. 前驱节点直接指向后驱节点，把target悬空
                # 此时待调整节点的前驱节点一定是sorted_tail
                sorted_tail.next = target.next
                # 2. 已知插入点和待调整的节点，修改待调整节点的next指针
                target.next = insert_point.next
                # 3. 最后修改插入点的next指针指向待调整的节点
                insert_point.next = target
            target = sorted_tail.next
        return dummy_head.next


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.insertionSortList(*tc))

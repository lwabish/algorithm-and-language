from typing import List, Optional
from lwabish.structs.listnode import ListNode, new_listnode, print_listnode
tcs = [
    (new_listnode([4, 2, 6, -1, 10]),),
    (new_listnode([1]),)
]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        # 初始：有序链表是从dummy到第一个节点
        sort_tail = head
        # 初始：待排序链表从第二个节点开始
        head = head.next

        while head:
            # 遍历从dummy到sort_tail的已有序的子链表，找到插入点
            p = dummy
            insert_p = sort_tail
            while p != sort_tail:
                if p.next and p.next.val > head.val:
                    insert_p = p
                    break
                p = p.next

            # 找到插入点后，断链重组
            # 备份插入点的后续节点
            insert_p_next = insert_p.next
            # 将插入点的后续节点改成待排序的节点
            insert_p.next = head
            # 备份待排序节点的后续节点
            head_next = head.next
            # 把待排序节点的后续节点改成插入点的原后续节点
            # 至此有序链表的更新完成
            head.next = insert_p_next

            # 完成后需要维护一下有序区间的右边界
            # 如果插入到了有序链表的中间，那不需要变
            if insert_p == sort_tail:
                # 如果插入到了有序链表的尾巴，那么新的右边界就是本轮排序的节点
                sort_tail = head

            # 之前我们把待排序的节点插入到别的地方后，可能发生断链的情况，重新连一下
            sort_tail.next = head_next
            # 准备继续排下一个节点
            head = sort_tail.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.insertionSortList(*tc))

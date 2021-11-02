from typing import List
from lwabish.structureutils.listnode import *
tcs = [
    (list(map(new_listnode, [[1, 4, 5], [1, 3, 4], [2, 6]])),),
]


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        合并排序链表数组

        """
        # 初始化一个list，把head都放进来
        heads = [listnode if listnode else None for listnode in lists]

        # 初始化result的头和尾
        result_head = ListNode()
        tail = result_head

        while heads != [None] * len(heads):
            this_node = ListNode()

            # 遍历heads，拿到最大值和其索引
            min_key = -1
            min_value = float("inf")
            for i, listnode in enumerate(heads):
                if listnode and listnode.val < min_value:
                    min_key, min_value = i, listnode.val

            # 最大值作为新node组装
            this_node.val = min_value
            tail.next = this_node

            # 更新tail
            tail = tail.next

            # 更新heads，把最大值所在链表的head往前推
            heads[min_key] = heads[min_key].next

        return result_head.next


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.mergeKLists(*tc))

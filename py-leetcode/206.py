from typing import List
from lwabish.structureutils.listnode import *
tcs = [
    (new_listnode([1, 2, 3]),),
    (new_listnode([1]),),
    (new_listnode([]),),
]


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        反转链表
        迭代法：关键问题是迭代过程中随着链的断开，会导致迭代循环被破坏。
        因此在基本的链表迭代基础上稍加修改，增加一个单独的变量存储迭代变量
        难点：while循环里的每一行顺序都不能乱，乱了状态就错了
        """
        last_node = None
        process_node = head
        while process_node:
            # 断链后会丢掉，存引用
            next_node = process_node.next
            # 反转，把当前迭代到的node的next改为last
            process_node.next = last_node
            # 把这轮的迭代变量更新给last node
            last_node = process_node
            # 更新迭代变量为下一个
            process_node = next_node
        return last_node


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.reverseList(*tc))

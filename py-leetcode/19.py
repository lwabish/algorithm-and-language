from typing import List
from my_data_structure import generate_linknode_from_list, print_linknode
from my_data_structure import LinkNode as ListNode
tcs = [
    (generate_linknode_from_list([1, 2, 3, 4, 5, 6]), 6),
]


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        last_node = None
        pointer = head
        to_delete = None
        while pointer:
            if eval('pointer' + '.next' * n) is None:
                to_delete = pointer
                break
            else:
                last_node = pointer
                pointer = pointer.next
        # 要删的是头结点
        if not last_node:
            return head.next
        # 要删的是尾节点
        if not to_delete.next:
            last_node.next = None
            return head
        # 要删的是中间节点
        last_node.next = to_delete.next
        to_delete.next = None
        return head


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_linknode(solution.removeNthFromEnd(*tc))

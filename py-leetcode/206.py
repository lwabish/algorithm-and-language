from typing import List
from my_data_structure import generate_linknode_from_list, print_linknode
tcs = [
    (generate_linknode_from_list([1, 2, 3, 4, 5]),),
]


new_head = None


# 递归，问题是需要在外面搞一个变量存尾节点
class Solution1:
    def reverseList(self, head):

        def reverse(node, last):
            if not node:
                global new_head
                new_head = last
                return
            reverse(node.next, node)
            node.next = last
        reverse(head, None)
        return new_head


# 多元赋值
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last_node = None
        node = head
        while node:
            node.next, last_node, node = last_node, node, node.next
        return last_node


if __name__ == '__main__':
    solution = Solution1()
    for tc in tcs:
        print_linknode(solution.reverseList(*tc))

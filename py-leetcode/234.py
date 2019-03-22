from typing import List
from my_data_structure import generate_linknode_from_list, print_linknode, LinkNode as ListNode
tcs = [
    (generate_linknode_from_list([1, 2, 3, 3, 2, 0]),),
    (generate_linknode_from_list([1, 2, 3, 4, 3, 2, 1]),),
    (generate_linknode_from_list([1]),),
    (generate_linknode_from_list([1, 2]),),
]


class Solution:
    # 方法1：快慢指针+倒转
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        p, last_node, p2 = head, None, head
        while p2 and p2.next and p2.next.next:
            p2 = p2.next.next
            p.next, p, last_node = last_node, p.next, p
        # 如果快指针不是停在最后，说明有偶数个节点，这时p在左半边上，需要让p再往前操作一步，否则左边少一个。
        # 如果快指针停在了最后，说明有奇数个节点，这时p正好在中间节点上，不需要操作。
        if p2.next:
            p.next, p, last_node = last_node, p.next, p
        # 如果是奇数个，p停在了中间节点，需要右移一下
        else:
            p = p.next

        # 经过快慢指针的操作，保证最后last_node停在已经反转的左半边的头结点上，p则是右半边的头结点。此时只需要对比这两个子链表是否一致即可。
        # print_linknode(last_node)
        # print_linknode(p)
        while p:
            if p.val != last_node.val:
                return False
            p, last_node = p.next, last_node.next
        return True


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isPalindrome(*tc))

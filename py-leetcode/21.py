from typing import List
from my_data_structure import generate_linknode_from_list, print_linknode, LinkNode
tcs = [
    (
        generate_linknode_from_list([1, 2, 3, 4]),
        generate_linknode_from_list([2, 4, 5, 6])
    ),
]


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            if l1.val < l2.val:
                new_head = l1
                l1 = l1.next
            else:
                new_head = l2
                l2 = l2.next
            current = new_head
        elif l1:
            return l1
        elif l2:
            return l2
        else:
            return None
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
            elif l1:
                current.next = l1
                l1 = l1.next
            elif l2:
                current.next = l2
                l2 = l2.next
            current = current.next
        return new_head


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_linknode(solution.mergeTwoLists(*tc))

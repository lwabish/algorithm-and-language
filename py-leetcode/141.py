from typing import List
from my_data_structure import generate_linknode_from_list
ln = generate_linknode_from_list([1, 2, 3, 4, 5])
head = ln
while head:
    if head.val == 3:
        entrance = head
    if head.val == 5:
        head.next = entrance
tcs = [
    (ln,),
    (generate_linknode_from_list([1, 2, 3, 4]),),
]


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1, p2 = head, head
        while p2.next:
            if p1 == p2 and p1 != head:


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.hasCycle(*tc))

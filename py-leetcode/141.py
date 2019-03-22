from typing import List
from my_data_structure import generate_linknode_from_list
ln = generate_linknode_from_list([1, 2, 3, 4, 5])
node = ln
while node:
    if node.val == 3:
        entrance = node
    if node.val == 5:
        node.next = entrance
        break
    node = node.next
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
        first_flag = True
        while p2:
            if p1 == p2:
                if first_flag:
                    first_flag = False
                else:
                    return True
            p1 = p1.next
            if not p2.next:
                p2 = p2.next
            else:
                p2 = p2.next.next
        return False


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.hasCycle(*tc))

from typing import List, Optional
from lwabish.structs.listnode import ListNode, print_listnode, new_listnode
tcs = [
    (),
]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.removeNthFromEnd(*tc))

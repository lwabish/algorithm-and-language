from typing import Optional
from lwabish.structs.listnode import ListNode
tcs = [
    ([1, 2, 2, 1]),
]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack == stack[::-1]


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isPalindrome(*tc))

from typing import List, Optional
tcs = [
    (),
]


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pass


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.copyRandomList(*tc))

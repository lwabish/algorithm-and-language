from typing import List, Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


tcs = [
    (Node(1),),
]


# 不难理解，但是很难想到
# 理解这题的关键：复制出来的新节点的random节点可能还不存在
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = {}

        def copy(head: 'Optional[Node]'):
            if not head:
                return None
            # 查缓存，找到对应关系并返回
            if cache.get(head):
                return cache.get(head)
            this = Node(head.val)
            # 缓存源节点和新节点的对应关系
            cache[head] = this
            this.next = copy(head.next)
            this.random = copy(head.random)
            return this
        return copy(head)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.copyRandomList(*tc))

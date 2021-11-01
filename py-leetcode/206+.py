from typing import List
from lwabish.structureutils.listnode import *
tcs = [
    (new_listnode([1, 2, 3]),),
    (new_listnode([1]),),
    (new_listnode([]),),
]


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        反转链表
        pythonic 极简风格
        两变量交换：

        a,b = b,a展开为
        t=a
        a=b
        b=t
        t为中间变量

        类推206可以看到循环体为
        n=q
        q=l
        l=p
        p=n
        n为循环变量
        因此可以改写成下面的形式
        p,q,l = q,l,p

        注意：python里的交换赋值是有顺序的，从左到右依次执行。在下面的3变量交换时，
        依然像206原循环体的顺序不能乱一样，交换的顺序也不能错。
        交换式相比于原循环体唯一的改进只是少声明了一个中间变量
        """
        last_node = None
        process_node = head
        while process_node:
            # 顺序：右边用完一个，左边就放这个变量换掉
            process_node.next, last_node,  process_node = last_node, process_node, process_node.next
        return last_node


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print_listnode(solution.reverseList(*tc))

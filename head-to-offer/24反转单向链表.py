from my_data_structure import generate_linknode_from_list, print_linknode
tc = [
    generate_linknode_from_list([1, 2, 3, 4, 5]),
    generate_linknode_from_list([1])
]


# 因为在主要的操作中，链表的next属性发生变化，所以为了避免混乱，应该单独使用变量先把自己和自己的下家保存起来，以便操作结束后更新指针为下一次迭代做准备。这里公用变量很容易乱掉，所以在循环里单独使用self_node和next_node保存当前迭代的自身和下一个节点
def main(linknode):
    last_node = None
    node = linknode
    while node:
        # 1.把自己存起来，用于后面更新lastnode指针
        self_node = node

        # 2.把自己的下一个节点存起来
        if not node.next:
            # 原尾节点例外，直接改变链接方向后返回即可
            node.next = last_node
            return node
        else:
            # 不是原尾节点的，都需要把下一个节点存起来
            next_node = node.next

        # 3.调整当前节点的next属性，实现反向
        if not last_node:
            # 原来的头结点只需要变成尾节点
            node.next = None
        else:
            # 中间节点需要反向链接
            node.next = last_node

        # 4.调整last指针，调整遍历指针
        last_node = self_node
        node = next_node


if __name__ == '__main__':
    for i in tc:
        print_linknode(main(i))

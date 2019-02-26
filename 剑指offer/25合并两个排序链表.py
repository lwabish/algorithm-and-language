from my_data_structure import generate_linknode_from_list, print_linknode

tc = [
    generate_linknode_from_list([1, 2, 3, 5, 7, 9]),
    generate_linknode_from_list([1, 2, 4, 5, 7, 8, 14])
]

tc = [
    generate_linknode_from_list([]),
    generate_linknode_from_list([])
]

tc = [
    generate_linknode_from_list([]),
    generate_linknode_from_list([1, 2, 4, 5, 7, 8, 14])
]

tc = [
    generate_linknode_from_list([1]),
    generate_linknode_from_list([14])
]


def main(head1, head2):
    head = None
    tail = None

    def cut_and_return_new_head(linknode):
        """
        切掉第一个节点
        返回：(切掉的第一个节点，后面的头结点)
        """
        if linknode.next:
            new_head = linknode.next
        else:
            new_head = None
        linknode.next = None
        return linknode, new_head

    def get_smaller_node(head1, head2):
        """
        根据head1 head2的大小情况，决定切掉谁
        返回((切掉的单节点,后面的头结点),被切掉的指针序号)
        """
        if not head1:
            return cut_and_return_new_head(head2), 2
        if not head2:
            return cut_and_return_new_head(head1), 1
        if head1.val < head2.val:
            return cut_and_return_new_head(head1), 1
        else:
            return cut_and_return_new_head(head2), 2

    while head1 or head2:
        # linknodes里包含被切掉的单节点，和新的头结点
        # cutted_head是1或2，决定了后面要更新head1还是head2
        linknodes, cutted_head = get_smaller_node(head1, head2)
        this_node = linknodes[0]
        new_head = linknodes[1]

        if head:
            # 拼接新链表
            tail.next = this_node
            tail = tail.next
        else:
            # 生成新链表
            head = tail = this_node

        # 根据谁被切了，移动指针，继续迭代
        if cutted_head == 1:
            head1 = new_head
        else:
            head2 = new_head
    return head


if __name__ == '__main__':
    print_linknode(main(tc[0], tc[1]))

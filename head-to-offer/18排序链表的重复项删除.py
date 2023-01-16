from my_data_structure import generate_linknode_from_list, print_linknode

# 普通测试用例
tc = generate_linknode_from_list([1, 2, 3, 3, 4, 4, 5, 6])
# 头重复
tc = generate_linknode_from_list([1, 1, 2, 3, 4, 4, 5])
# 尾重复
tc = generate_linknode_from_list([1, 2, 3, 4, 4])
# 两位不重复
tc = generate_linknode_from_list([1, 2])
# 两位重复
tc = generate_linknode_from_list([1, 1])
# 单节点
tc = generate_linknode_from_list([1])
# 全部是都是重复的
tc = generate_linknode_from_list([1, 1, 1, 1, 1, 1])


def main(head):
    # 只有一个节点的链表，不需要去重
    if not head.next:
        return head

    # 得到不重复的头结点
    def set_real_head(head):
        """
        找到第一个非重复的节点作为结果的头结点\n
        输入链表的长度大于1\n
        return None:全是重复的，LinkNode:第一个不和后面重复的节点\n
        """
        while head:
            if not head.next:
                return None
            if head.val == head.next.val:
                head = head.next.next
                continue
            return head
    real_head = set_real_head(head)

    # 如果没有头结点，说明全是重复的
    if not real_head:
        print('全部重复')
        return
    print('头结点是')
    print_linknode(real_head)

    # node指针是遍历指针，last_node指向不重复的最后一个节点
    node, last_node = real_head, None
    while node.next:
        if node.val == node.next.val:
            # 重复节点不在末尾
            if node.next.next:
                # 重新链接
                last_node.next = node.next.next
                # 修改遍历方向
                node = node.next.next
            # 重复节点在末尾
            else:
                last_node.next = None
                return real_head
        else:
            # 如果当前遍历到的节点没和下一个节点重复，则更新last_node
            last_node = node
            # 继续遍历
            node = node.next
    return real_head


if __name__ == '__main__':
    print_linknode(main(tc))

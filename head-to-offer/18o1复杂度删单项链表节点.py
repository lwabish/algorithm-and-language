from my_data_structure import generate_random_linknode, print_linknode, get_random_node, generate_linknode_from_list, get_specific_linknode

# 正常测试用例
tc = generate_random_linknode(10, 3)
tc_del = get_random_node(tc)
print('原始单项链表为：')
print_linknode(tc)
print('要删除的节点为：')
print_linknode(tc_del)

# 删除尾巴节点
tc = generate_linknode_from_list([1, 2, 3, 4, 5])
tc_del = get_specific_linknode(tc, 5)
print('原始单项链表为：')
print_linknode(tc)
print('要删除的节点为：')
print_linknode(tc_del)

# 只有一个节点的单项链表删除节点
tc = generate_linknode_from_list([1])
tc_del = get_specific_linknode(tc, 1)
print('原始单项链表为：')
print_linknode(tc)
print('要删除的节点为：')
print_linknode(tc_del)

# 正常删除需要找到要删除节点的上一个节点，需要遍历。
# 所以为了实现O1复杂度的删除，要在下一个节点做手脚：用待删除节点的下一个节点覆盖掉待删除节点即可。


def main(head, del_node):
    # 只有一个节点的单项链表，只能删除头结点
    if head.next == None:
        print('删除完为空')
        return
    # 要删除的是最后一个节点，还需要遍历得到并修改上一个节点
    if del_node.next == None:
        node = head
        while node:
            if node.next == del_node:
                node.next = None
            node = node.next
    # 要删除的不是尾巴节点
    else:
        del_node.val = del_node.next.val
        del_node.next = del_node.next.next
    print('删除后的单向链表为：')
    print_linknode(head)


if __name__ == '__main__':
    main(tc, tc_del)

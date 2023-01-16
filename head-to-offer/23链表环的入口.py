from my_data_structure import generate_linknode_from_list, print_linknode, linknode_add_circle, LinkNode

# 有环
# 入口在中间
tc = linknode_add_circle(generate_linknode_from_list([1, 2, 3, 4, 5, 6, 7]), 4)
# 入口在末尾（尾巴节点不能连接自己）
tc = linknode_add_circle(generate_linknode_from_list([1, 2, 3, 4, 5, 6, 7]), 6)
# 入口在开头
tc = linknode_add_circle(generate_linknode_from_list([1, 2, 3, 4, 5, 6, 7]), 1)


# 无环
tc = generate_linknode_from_list([1, 2, 3])
tc = generate_linknode_from_list([1])


def main(linknode):
    inside_counter = set()
    while linknode:
        if linknode in inside_counter:
            return linknode
        inside_counter.add(linknode)
        linknode = linknode.next
    return '该单向链表没有环'


if __name__ == '__main__':
    res = main(tc)
    if type(res) == LinkNode:
        print(res.val)
    else:
        print(res)

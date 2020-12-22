from my_data_structure import generate_linknode_from_list, print_linknode

# 每隔K个反转链表
# 关键问题：一边遍历一边修改的话，会影响遍历。
tc = [
    generate_linknode_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    generate_linknode_from_list(list(range(1))),
]


# 解决：先遍历，将要修改next的节点成对放到元组里。遍历完成后再批量修改
# 这种方法要求k>1。k=1时失效。k=1则退化成了反转单项链表的问题
def main(linknode, k):
    # 先对要修改next指针的节点进行配对，放进元组中。
    pairs = list()
    last_head = list()
    new_tail_found = False
    counter = 1
    while linknode:
        if counter % k == 1:
            last_head.append(linknode)
        elif counter % k == 0:
            if not new_tail_found:
                this_pair = (linknode, None)
                new_tail_found = True
            else:
                this_pair = (linknode, last_head.pop(0))
            pairs.append(this_pair)
        elif not linknode.next:
            pairs.append((linknode, last_head.pop(0)))
        counter += 1
        linknode = linknode.next

    # 遍历配对元组，把该修改的指针修改掉
    for pair in pairs:
        pair[0].next = pair[1]
    return last_head[0]


if __name__ == '__main__':
    for i in tc:
        print_linknode(main(i, 2))

from my_data_structure import generate_linknode_from_list, print_linknode
# 注意陷阱：K可能大于链表的长度！
tc = generate_linknode_from_list([1, 2, 3, 4, 5, 6, 7])
tc_k = 0
tc_k = 3
tc_k = 7
tc_k = 8


tc = generate_linknode_from_list([1])
tc_k = 0
tc_k = 1
tc_k = 2


# python的负索引：遍历一遍，依次加入列表，最后用负索引索引出来即可。
def main_py(linknode, k):
    nodes = list()
    while linknode:
        nodes.append(linknode)
        linknode = linknode.next
    if k > len(nodes):
        return 'k太大'
    elif k < 1:
        return 'k太小'
    return nodes[-k]


# 双指针法，算出一个在尾巴，一个在目标值时的距离，然后一开始控制两个指针的距离，达到指定距离后，一起往后走，前面的指针在尾巴上以后，后面的指针就是结果。
# n-x=n-k+1   n是尾巴，n-k+1是目标节点的正数顺序
# x = k-1   所以两个指针应该预先保持k-1的距离
def main(linknode, k):
    if k < 1:
        return 'k太小啦'
    index_front, index_behind = 0, 0
    node_front, node_behind = linknode, linknode
    while index_front - index_behind < k - 1:
        # k不超过链表长度的时候，前面指针最多走到末尾节点，循环就不会继续了。
        # 一旦k超过链表长度，再进入循环时前面指针已经在末尾了。这时就说明k太大了。
        if not node_front.next:
            return 'K太大啦'

        index_front += 1
        node_front = node_front.next

    # 验证经过循环后，两个指针是否拉开了k-1的差距
    # print(index_front-index_behind, k-1)

    # 一起前进，直到
    while node_front.next:
        node_front = node_front.next
        node_behind = node_behind.next
    return node_behind


if __name__ == '__main__':
    print_linknode(main(tc, tc_k))
    print_linknode(main_py(tc, tc_k))

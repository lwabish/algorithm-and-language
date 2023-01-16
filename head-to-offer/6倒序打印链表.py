from my_data_structure import generate_random_linknode, print_linknode, Stack

tc = generate_random_linknode(5, 5)  # 生成一个长度为5，值在1-5之间的随机链表
print_linknode(tc)


# 方法1：利用栈后进先出的特点
def main(node):
    stack = Stack()
    while node != None:
        # print(node.val)
        stack.add(node.val)
        if node.next != None:
            node = node.next
        else:
            node = None
    while stack:
        print(stack.pop())


# 方法2：利用递归调用栈倒序的特点倒序打印，但是链太长可能导致溢出，鲁棒性不好
def main2(node):
    if node == None:
        return
    main2(node.next)
    print(node.val)


if __name__ == '__main__':
    main(tc)
    # main2(tc)

from my_data_structure import generate_treenode, print_treenode
tc = [
    generate_treenode('7,3,15,null,null,9,20')
]


class BSTIterator:

    def __init__(self, root):
        if root:
            self.mid_order_list = [
                int(i) for i in self.mid_order_to_list(root)[:-1].split(',')]
        else:
            self.mid_order_list = []

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.mid_order_list.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.mid_order_list:
            return True
        else:
            return False

    def mid_order_to_list(self, root):
        if not root:
            return ''
        return self.mid_order_to_list(root.left)+str(root.val)+','+self.mid_order_to_list(root.right)


if __name__ == '__main__':
    obj = BSTIterator(tc[0])

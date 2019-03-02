from my_data_structure import generate_treenode, print_treenode, TreeNode
tc = [
    generate_treenode('5,3,6,2,4,null,7'),
    generate_treenode('1,null,2'),
    generate_treenode('1,null,2'),
    generate_treenode('0'),
    generate_treenode('5,3,6,2,4,null,7'),
    generate_treenode('2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6')
]
print_treenode(tc[5])


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        self.head = root

        def get_mid_order_next(root: TreeNode, parent: TreeNode):
            """
            返回一个节点的中序遍历的下一个节点及其父节点。
            注意：这里的算法只是这道题适用，因为在题里找中序遍历下一个节点时一定有右子节点，这是所有找中序遍历下一个节点的算法中的一种情况。
            """
            while root.left:
                return get_mid_order_next(root.left, root)
            return root, parent

        def delete(root, key, parent: TreeNode):
            # 没找到
            if not root:
                return None
            if root.val > key:
                delete(root.left, key, root)
            elif root.val < key:
                delete(root.right, key, root)
            else:
                # 要删除的节点没有子节点
                if not root.left and not root.right:
                    if not parent:
                        self.head = None
                        return
                    if parent.left and parent.left.val == key:
                        parent.left = None
                    elif parent.right and parent.right.val == key:
                        parent.right = None
                    return
                # 要删除的节点有一个子节点
                if not root.left and root.right:
                    if not parent:
                        self.head = root.right
                        return
                    if parent.left and parent.left.val == root.val:
                        parent.left = root.right
                    elif parent.right and parent.right.val == root.val:
                        parent.right = root.right
                    return
                elif not root.right and root.left:
                    if not parent:
                        self.head = root.left
                        return
                    if parent.left and parent.left.val == root.val:
                        parent.left = root.left
                    elif parent.right and parent.right.val == root.val:
                        parent.right = root.left
                    return
                # 要删除的节点有两个子节点，结合剑指offer里的求节点中序遍历的下一个节点，这里是那道题的一种最简单的情况：即有右子节点的情况下，找中序遍历的下一个节点。只需要从右子节点开始一路向左到底即可得到要找的节点。
                mid_order_next, mid_order_next_parent = get_mid_order_next(
                    root.right, root)
                root.val = mid_order_next.val
                if mid_order_next_parent == root:
                    if mid_order_next.right:
                        root.right = mid_order_next.right
                    else:
                        root.right = None
                else:
                    delete(mid_order_next, mid_order_next.val,
                           mid_order_next_parent)

        delete(root, key, None)
        return self.head


if __name__ == '__main__':
    print_treenode(Solution().deleteNode(tc[5], 33))
    print_treenode(generate_treenode('2,0,34,null,1,25,40,null,null,11,31,35,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,null,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,38,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6'))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    r = list()
    if head == None:
        return []
    while head.next != None:
        # print(head.val,head.next.val)
        if head.next.val == head.val and head.next.next != None:
            head.next = head.next.next
            continue
        elif head.next.val == head.val and head.next.next == None:
            head.next = None
            continue
        r.append(head.val)
        if head.next != None:
            head = head.next
    r.append(head.val)
    return r

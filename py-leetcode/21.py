# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    nums = []
    while l1 != None:
        nums.append(l1.val)
        l1 = l1.next
    while l2 != None:
        nums.append(l2.val)
        l2 = l2.next
    if len(nums) == 0:
        return ListNode('')
    nums.sort()
    result = list(range(len(nums)))
    for t in range(len(nums)-1, -1, -1):
        # print(t)
        result[t] = ListNode(nums[t])
        if t != len(nums)-1:
            result[t].next = result[t+1]
    return result[0]

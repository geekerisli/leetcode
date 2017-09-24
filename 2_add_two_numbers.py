# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = t = ListNode(0)	
        while l1 or l2 or carry:
            s1 = s2 = 0
            if l1:
                s1 = l1.val
                l1 = l1.next
            if l2:
                s2 = l2.val
                l2 = l2.next
            carry, val = divmod(s1+s2+carry, 10)
            t.next = ListNode(val)
            t = t.next
        return root.next

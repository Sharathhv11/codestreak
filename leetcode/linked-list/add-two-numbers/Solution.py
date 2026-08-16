# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        p1 = l1
        p2 = l2
        dummy = ListNode(val=0,next=None)
        p = dummy

        carry = 0
        while( p1 is not None and p2 is not None ):
            total = p1.val + p2.val + carry

            q  = total // 10 
            r = total % 10 

            p.next = ListNode(r)
            p = p.next
            carry = q

            p1 = p1.next
            p2 = p2.next

        while( p1 is not None ):
            total = carry + p1.val 

            q  = total // 10 
            r = total % 10 

            p.next = ListNode(r)
            p = p.next
            carry = q
            p1 = p1.next
        while( p2 is not None ):
            total = carry + p2.val 

            q  = total // 10 
            r = total % 10 

            p.next = ListNode(r)
            carry = q
            p = p.next
            p2 = p2.next

        if( carry != 0 ):
            p.next = ListNode(carry)

        return dummy.next







        
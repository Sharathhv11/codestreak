# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        previous = ListNode()
        previous.next = node

        p = previous 
        i = node

        while( i.next is not None ):
            i.val,i.next.val = i.next.val,i.val
            i = i.next
            p = p.next

        p.next = None
        previous.next = None

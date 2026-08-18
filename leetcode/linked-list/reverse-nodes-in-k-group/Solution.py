# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self,start,end):
        lastInReverse = start

        p = start
        previous = None

        while( p != end ):
            nextInList = p.next 
            p.next = previous 
            previous = p
            p = nextInList

        p.next = previous 

        return p,lastInReverse



    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        count = 0
        p = head
        start = head 
        tail = None

        nHead = None

        while( p is not None ):
            count+=1 

            if( count == k ):
                count = 0
                nextSet = p.next 
                headInReverse,lastInReverse =self.reverse(start,p)
                print(headInReverse.val)
                print(lastInReverse.val)

                if( nHead is None ):
                    nHead = headInReverse

                if( tail is None ):
                    tail = lastInReverse
                else:
                    tail.next = headInReverse
                    tail = lastInReverse

                start = nextSet
                p = nextSet


            else:
                p = p.next

        tail.next = start

        return nHead

            
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # place the curr_ptr on the nth node from the starting
        curr_ptr = head
        for i in range(n-1):
            curr_ptr = curr_ptr.next
        
        # point lastn at the head (will point on the node to be deleted)
        # temp node will point to left node of lastn
        lastn = head
        temp = None
        # iterate through the list until curr_ptr reach to the end of the list, and with each iteration move temp and lastn one step ahead
        while curr_ptr.next != None:
            curr_ptr = curr_ptr.next
            temp = lastn
            lastn = lastn.next
        
        # now remove lastn node (which will be nth node from the last at this point)
        if temp:
            temp.next = lastn.next
            lastn.next = None
        else:
            head = head.next
            lastn.next = None

        return head
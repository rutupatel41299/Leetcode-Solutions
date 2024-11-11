# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if number of elements in the list is 0 or 1, return head.
        if head == None:
            return head
        if head.next == None:
            return head
        
        # store the current value and iterate through the list.
        # if the current value is repeated remove that node, else store the value of curr element in the list as current value to be checked
        cur_val = head.val
        temp = head
        lst = head.next
        while lst != None:
            if lst.val == cur_val:
                if lst.next != None:
                    temp.next = lst.next
                    x = lst.next
                    lst.next = None
                    lst = x
                else:
                    temp.next = None
                    lst = lst.next
            else:
                cur_val = lst.val
                temp = lst
                lst = lst.next
        
        return head
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
        answer = ListNode()
        temp = answer
        carry = 0

        # iterate through both the linked list until one of them is empty.
        # create the answer list by appending the last digit of sum of list1 and list2, and store first digit as carry to add it in the sum with next iteration.
        while l1 != None and l2 != None:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            x = ListNode(sum % 10, None)
            temp.next = x
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        # check if any list is non empty, add the element of it with answer list by summing it up with last carry.
        while l1 != None:
            sum = l1.val + carry
            carry = sum // 10
            x = ListNode(sum % 10, None)
            temp.next = x
            temp = temp.next
            l1 = l1.next
        
        while l2 != None:
            sum = l2.val + carry
            carry = sum // 10
            x = ListNode(sum % 10, None)
            temp.next = x
            temp = temp.next
            l2 = l2.next

        if carry != 0:
            x = ListNode(carry, None)
            temp.next = x
        
        return answer.next
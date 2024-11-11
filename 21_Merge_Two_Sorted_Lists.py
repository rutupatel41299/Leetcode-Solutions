# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if any list is empty, return another list
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        # if initial value of list2 is less than list1, make list2 answerhead and append list 1 after that node. else do the opposite.
        # then iterate through list1, if the current list2 val is less then current list1 value, append current list2 node before current list1 node.
        if list2.val <= list1.val:
            answerHead = list2
            list2 = list2.next
            answerHead.next = list1
            temp = answerHead
            while list2 != None and list1 != None:
                if list2.val <= list1.val:
                    newNode = list2
                    list2 = list2.next
                    temp.next = newNode
                    newNode.next = list1
                    temp = temp.next
                else:
                    temp = list1
                    list1 = list1.next
            if list2 != None:
                temp.next = list2
            return answerHead
        else:
            answerHead = list1
            list1 = list1.next
            answerHead.next = list2
            temp = answerHead
            while list2 != None and list1 != None:
                if list1.val <= list2.val:
                    newNode = list1
                    list1 = list1.next
                    temp.next = newNode
                    newNode.next = list2
                    temp = temp.next
                else:
                    temp = list2
                    list2 = list2.next
            if list1 != None:
                temp.next = list1
            return answerHead
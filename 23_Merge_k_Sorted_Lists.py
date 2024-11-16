# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # if lenth of lists is 0, return none and if it is 1, ret
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        # create an answer linked list with initial node value 0 (at the and return the second node of the ans)
        answer = ListNode()
        temp = answer

        heap = []
        # iterate through the lists and push the value of first node from each list
        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(heap, (lists[i].val, i))
        
        # pop the smallest element from the heap and append it to the answer, then push the first element from the same list index to the heap and repeat the process untill list is empty.
        while len(heap) != 0:
            mi, idx = heapq.heappop(heap)
            new_node = lists[idx]
            lists[idx] = lists[idx].next
            new_node.next = None
            temp.next = new_node
            temp = temp.next

            if lists[idx] != None:
                heapq.heappush(heap, (lists[idx].val, idx))
        
        return answer.next

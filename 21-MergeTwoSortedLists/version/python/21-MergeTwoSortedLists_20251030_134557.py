# Last updated: 10/30/2025, 1:45:57 PM
# Two Pointers.  Using a dummy node, iterate over both lists and compare the results, change the link direction to form a new linked list. O(N) Time, O(1) Space.
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
        curr = dummy_head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1 #point to the smaller list
                # update the remain list and current pointer
                list1 = list1.next
                curr = curr.next # move the current pointer to the new combined list
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        
        #Check if any node left after while loop
        if list1 or list2:
            curr.next = list1 if list1 else list2

        return dummy_head.next

                
        
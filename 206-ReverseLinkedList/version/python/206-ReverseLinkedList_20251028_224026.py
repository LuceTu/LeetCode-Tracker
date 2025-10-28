# Last updated: 10/28/2025, 10:40:26 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head

        while curr!= None:

            # move next_pointer to the right
            next_pointer = curr.next

            # make curr point to the prev
            curr.next = prev

            # update curr & prev
            prev = curr
            curr = next_pointer
        
        head = prev
        
        return prev


        
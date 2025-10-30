# Last updated: 10/30/2025, 12:48:20 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = fast = head
        while fast and fast.next: # remember to check fast.next cuz it might None.next will cause AttributeError (FAILS for odd length )
            slow = slow.next
            fast = fast.next.next
        return slow


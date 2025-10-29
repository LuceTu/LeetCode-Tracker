# Last updated: 10/29/2025, 6:40:06 PM
'''
Using a dummy_head helps solve edge cases(head node deleting).
A node reference points to the entire remaining chain, not just a single node.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        dummy_head = ListNode(-1)
        dummy_head.next = head

        current_node = dummy_head

        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
            
        return dummy_head.next
        
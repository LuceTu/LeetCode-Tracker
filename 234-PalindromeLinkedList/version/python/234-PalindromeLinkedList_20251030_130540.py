# Last updated: 10/30/2025, 1:05:40 PM
# Middle of the Linked List + Reverse Linked List + Two pointers
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # Step 1: Find the middle of the linked list
        fast = head
        slow = head 
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next 
        
        # Step 2: Reverse the second half
        prev = None
        
        while slow:
            next_pointer = slow.next

            slow.next = prev # Reverse the link 

            # update the prev and curr(slow)
            prev = slow
            slow = next_pointer
        
        # Step 3: Check palindrome using two pointers
        left = head
        right = prev # prev is the head of the reversed second half (= the last one)
        while right:
            # Check each node's value
            if left.val != right.val:
                return False 
            
            #update the two pointer to the middle
            left = left.next
            right = right.next
        
        return True
            



            

        
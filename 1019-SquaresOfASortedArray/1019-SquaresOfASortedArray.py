# Last updated: 10/26/2025, 4:57:07 PM
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_p = 0
        right_p = len(nums) - 1
        answer = collections.deque()

        while left_p <= right_p:
            l , r = abs(nums[left_p]), abs(nums[right_p])
            if l <= r:
                answer.appendleft(r*r)
                right_p -= 1
            else:
                answer.appendleft(l*l)
                left_p += 1
        
        return list(answer)
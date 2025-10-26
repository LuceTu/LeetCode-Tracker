# Last updated: 10/26/2025, 4:57:05 PM
class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n % 2 != 0:
            return n*2
        else:
            return n
        
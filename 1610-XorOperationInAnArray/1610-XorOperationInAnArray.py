# Last updated: 10/26/2025, 4:57:04 PM
class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        result = 0
        for i in range(n):
            result =  result ^ (start + 2 * i)
        return result


        
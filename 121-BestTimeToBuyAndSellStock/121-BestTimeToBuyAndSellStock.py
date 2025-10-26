# Last updated: 10/26/2025, 4:57:14 PM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r = 0,1
        maxP = 0

        while r != len(prices):
            if prices[l] < prices[r]:
                prof = prices[r]-prices[l]
                maxP = max(prof,maxP)
            else:
                l = r
            r+=1
        
        return maxP
        
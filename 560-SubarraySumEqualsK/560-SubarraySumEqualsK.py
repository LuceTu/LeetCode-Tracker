# Last updated: 10/26/2025, 4:57:09 PM
class Solution(object):
    
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        prefix_count = {0: 1} #手动把原点写进去 避免不存在的key
        result = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            if (curr_sum - k) in prefix_count:
                result += prefix_count[curr_sum - k]
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1
        return result
# Last updated: 10/26/2025, 4:57:15 PM
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort() #排序去重
        res = []

        for i in range(len(nums)-2): #注意边界问题，后面要有双指针，所以至少要留下两个数字
            if i > 0 and nums[i] == nums[i-1]: #去重
                continue
            
            left = i + 1
            right = len(nums) -1

            while left < right :
                total = nums[i]+nums[left]+nums[right] 

                if total == 0:
                    res.append([nums[i],nums[left],nums[right]]) #返回的数据要按照要求的格式
                
                    while left < right and nums[left] == nums[left+1]: #左指针去重
                        left += 1 
                    while left < right and nums[right] == nums[right-1]: #右指针去重
                        right -=1    
                    
                    left += 1 #结果append 之后记得移动指针
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -=1
            
        return res
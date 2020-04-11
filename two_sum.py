# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            complement = target - num
            
            # First, check whether complement equals num
            if complement == num:
                indices = [index for index, value in enumerate(nums) if value == num]
                return indices if len(indices) > 1
                
            elif complement in nums:
                j = nums.index(complement)
                return [i,j]
            

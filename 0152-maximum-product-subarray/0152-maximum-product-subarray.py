class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = min_sum = return_value = nums[0] 
         
        for i in range(1, len(nums)):
            candidates = (nums[i], max_sum*nums[i], min_sum*nums[i])
            max_sum = max(candidates)
            min_sum = min(candidates)
            return_value = max(max_sum, return_value)
        return return_value
        
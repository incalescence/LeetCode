class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return_array = [1]*len(nums)
        
        # pass through front to back to store prefix product
        pre_product = nums[0]
        for i in range(1,len(nums)):
            return_array[i] = pre_product
            pre_product *= nums[i]
        
        # pass through back to front storing postfix produc
        post_product = 1
        for j in reversed(range(0,len(nums))):
            return_array[j] *= post_product
            post_product *= nums[j]
            
        return return_array
class Solution:
    # linear sliding window technique to get net positive
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_total = 0
        
        for n in nums:
            if curr_total < 0:
                curr_total = 0
            curr_total += n 
            max_sum = max(max_sum,curr_total)

        return max_sum
        
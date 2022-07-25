class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        og_size = len(nums)
        for i in range(og_size):
            nums.append(nums[i])
        return nums 
            
        
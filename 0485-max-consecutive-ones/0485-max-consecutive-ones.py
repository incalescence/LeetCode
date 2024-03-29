class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0;
            if count > max_count:
                max_count = count            
        return max_count
        
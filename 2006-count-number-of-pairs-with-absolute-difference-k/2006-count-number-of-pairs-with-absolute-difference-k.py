class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        size = len(nums)
        count = 0 
        for i in range(size):
            for j in range(i+1, size):
                if abs(nums[i]-nums[j]) == k:
                    count += 1
        return count 
        
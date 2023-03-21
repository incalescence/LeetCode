class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        no_duplicates = list(set(nums))
        no_duplicates.sort(reverse=True)
        if len(no_duplicates) >= 3:
            return no_duplicates[2]
        else: 
            return max(nums)
        
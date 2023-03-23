class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicates = list(set(nums))
        no_duplicates.sort(reverse=True)
        if len(no_duplicates) >= 3:
            return no_duplicates[2]
        else: 
            return max(nums)
        
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_array = sorted(nums)
        return max(sorted_array[-1]*sorted_array[-2]*sorted_array[-3],sorted_array[0]*sorted_array[1]*sorted_array[-1])
        
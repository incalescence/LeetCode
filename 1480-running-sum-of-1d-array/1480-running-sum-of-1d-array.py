class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return_list = []
        sum = 0
        for i in nums:
            sum += i 
            return_list.append(sum)
        return return_list 
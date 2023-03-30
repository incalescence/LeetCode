class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if nums[i] in d:
                return ([i, d.get(nums[i])])
            d[dif] = i
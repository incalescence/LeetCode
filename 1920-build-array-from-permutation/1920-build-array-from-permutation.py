class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        arr = []
        for i in range(size):
            arr.append(nums[nums[i]])
        return arr
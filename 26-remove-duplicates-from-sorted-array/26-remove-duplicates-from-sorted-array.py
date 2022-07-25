class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:]=sorted(set(nums),key = nums.index)
        return len(nums)
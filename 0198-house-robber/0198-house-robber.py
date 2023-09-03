class Solution:
    def rob(self, nums: List[int]) -> int:
        loot = 0
        for i in range(len(nums)):
            if i == 2:
                nums[i] += nums[0]
            if i > 2:
                nums[i] += max(nums[i-2], nums[i-3])
            loot = max(nums[i], loot)
        return loot
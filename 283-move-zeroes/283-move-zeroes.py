class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for number in nums:
            if number == 0:
                nums.remove(0)
                nums.append(0)
        
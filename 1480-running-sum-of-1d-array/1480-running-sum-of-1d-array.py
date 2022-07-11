class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            arr.append(sum)
        return arr
            
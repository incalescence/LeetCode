class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return_list = []
        for num in nums:
            index = abs(num)-1
            if nums[index] > 0:
                nums[index] *=-1
            else:
                return_list.append(abs(num))
        return return_list[0]
            
            
        
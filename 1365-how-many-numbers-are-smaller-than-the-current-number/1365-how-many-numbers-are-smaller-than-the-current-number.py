class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return_list = []
        for i in nums:
            count = 0 
            for k in nums:
                if k < i:
                    count+=1
            return_list.append(count)
        return return_list 
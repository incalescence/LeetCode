class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return_list = []
        for num in nums:
            return_list.append(num*num)
        return sorted(return_list)
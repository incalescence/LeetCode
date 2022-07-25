class Solution(object):
    def singleNumber(self, nums):
        freq = {}
        return_list = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for k in freq:
            if freq[k] == 1:
                return_list.append(k)
        return return_list
                
                
        
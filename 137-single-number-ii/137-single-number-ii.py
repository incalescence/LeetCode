class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        return min(freq, key=freq.get)
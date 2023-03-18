import collections

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        counter = Counter(nums)
        for key in counter:
            if counter[key] == 2:
                duplicates.append(key)
        return duplicates
        
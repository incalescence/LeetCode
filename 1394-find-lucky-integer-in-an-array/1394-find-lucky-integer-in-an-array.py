from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = Counter(arr)
        return max([k for k, v in hashmap.items() if k == v] + [-1])
        
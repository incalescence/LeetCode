# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        high = n-1
        low = 0
        while(low <= high):
            mid = int(low + (high - low)/2)
            if isBadVersion(mid) != True:
                low = mid + 1
            else:
                high = mid - 1
        return low
        
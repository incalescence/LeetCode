class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range (len(s)):    
            try:
                index = t.index(s[i])
            except ValueError: 
                return False
            t = t[index+1:]
        return True
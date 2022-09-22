class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = Counter(s)
        
        longest_palindrome = 0
        # even case add all even and add odd -1 
        for value in s_dict.values():
            longest_palindrome += value
            if (value%2==1):
                longest_palindrome -= 1
        
        if longest_palindrome + 1 <= len(s):
            return (longest_palindrome + 1)
        
        else: 
            return longest_palindrome
            
        
        
        
        
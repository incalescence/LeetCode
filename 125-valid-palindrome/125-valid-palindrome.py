import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        all_letters = ''
        for char in s:
            if char.isalnum():
                all_letters += char 
        all_letters_reversed = all_letters[::-1]
        if all_letters_reversed == all_letters:
            return True 
        return False 
        
        
        
        
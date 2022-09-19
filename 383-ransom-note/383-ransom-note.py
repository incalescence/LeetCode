from collections import Counter 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_dict = Counter(ransomNote)
        magazine_dict = Counter(magazine)
        magazine_dict.subtract(note_dict)  
        if any(value < 0 for value in magazine_dict.values()):
            return False     
        return True 
                

        
        
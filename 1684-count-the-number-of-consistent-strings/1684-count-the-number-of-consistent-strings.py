class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0
        allowed_set = set(allowed)
        for string in words:
            if set(string).issubset(allowed_set):
                counter += 1
        return counter
                
                
        
        
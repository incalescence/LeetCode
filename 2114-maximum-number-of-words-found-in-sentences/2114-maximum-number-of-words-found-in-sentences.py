class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for sentence in sentences:
            length = len(sentence.split(' '))
            if length > max:
                max = length
        return max
        
    
        
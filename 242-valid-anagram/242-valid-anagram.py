class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     
        data_s = {}
        for i in s:
            if i not in data_s:
                data_s[i]=0
            else:
                data_s[i]+=1
        data_t = {}
        for i in t:
            if i not in data_t:
                data_t[i]=0
            else:
                data_t[i]+=1
        
        if data_s == data_t:
            return True
        else:
            return False
                
            
        
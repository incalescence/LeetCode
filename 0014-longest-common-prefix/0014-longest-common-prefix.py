class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # empty array 
        if len(strs) == 0:
            return ''
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            if len(strs[i]) < len(prefix):
                prefix = prefix[0:len(strs[i])]
            for j in range(len(prefix)):
                if prefix[j] != strs[i][j]:
                    if j == 0:
                        prefix = ''
                    else:
                        prefix = prefix[0:j]
                    break
                # if j == len(strs[i])-1:
                #     prefix = strs[i]
                #     break
        return prefix

            
            
        
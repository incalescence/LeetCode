class Solution:  
    @cache
    def climbStairs(self, n: int) -> int:
        #base cases
        if (n == 1):
            return 1
        elif (n == 2):
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
            
        
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        DP = []
        # subproblem: minimum cost to get to that step 
        # recursive case: dp[i] = cost[i] + min(dp[i-2], dp[i-1])
        # base case: cost to get to step1 or step 2
        
        for i in range(len(cost)):
            if i == 0 or i == 1:
                DP.append(cost[i])
            else:
                DP.append(cost[i]+min(DP[i-1],DP[i-2]))
        return min(DP[-1], DP[-2])
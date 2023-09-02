class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        DP = []
        for i in range(len(cost)):
            if i == 0 or i == 1:
                DP.append(cost[i])
            else:
                DP.append(cost[i]+min(DP[i-1],DP[i-2]))
        return min(DP[-1], DP[-2])
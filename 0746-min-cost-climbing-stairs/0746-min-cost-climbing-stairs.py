class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # adding last index
        # ex : [10, 15, 20]_0_
        cost.append(0)
        # since we are at index three it does not take any cost to reach there
        # so cost is 0
        
        # starting from 15 (index:1)
        for i in range(len(cost) - 3, -1, -1):
            
            # min of taking 1/2 jump(s)
            
            cost[i] += min(cost[i+1], cost[i+2])
            
        # since we can start from both index 0 and 1    
        return min(cost[0], cost[1])
                
            
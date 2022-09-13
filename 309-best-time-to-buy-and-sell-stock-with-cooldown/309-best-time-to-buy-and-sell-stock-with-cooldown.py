class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # dp = { [(i, canBuy)] : max_profit }
        dp = {}
        def max_p(i, canBuy):
                        
            if i >= len(prices):
                return 0
            
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            
            if canBuy:
                # 2 options buy/ cooldown then take max
                buy = max_p(i + 1, not canBuy) - prices[i]
                cooldown = max_p(i + 1, canBuy)
                dp[(i, canBuy)] = max(buy, cooldown)
                
            else:
                # skip one element coz we need to cooldown
                sell = max_p(i+2, not canBuy) + prices[i]
                cooldown = max_p(i + 1, canBuy)
                dp[(i, canBuy)] = max(sell, cooldown)

            return dp[(i, canBuy)]
        
        return max_p(0, True)
            
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # we just need to look at last two values of max sums
        
        rob1, rob2 = 0, 0
        
        # [rob1, rob2, n, n + 1, ...]
        # choose from (rob1,n) or just rob2 since adjacent rule
        for num in nums:
            res = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = res
            
        return rob2
        
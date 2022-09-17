class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache = {} # key : (i, total) ; value : No. of ways
        
        def backtrack(i, total):
            
            # base case, we iterate over entire array 
            if i == len(nums):
                return 1 if total == target else 0

            if (i, total) in cache:
                return cache[(i, total)]
            
            cache[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
            
            return cache[(i, total)]
        
        
        return backtrack(0,0)
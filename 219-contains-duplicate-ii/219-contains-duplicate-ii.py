class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        cache = {}
        
        for index, num in enumerate(nums):
            if num in cache and abs(index - cache[num]) <= k:
                return True
            
            cache[num] = index
            
        return False
        
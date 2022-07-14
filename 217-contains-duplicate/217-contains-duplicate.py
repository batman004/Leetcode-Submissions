class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        cache = {}
        
        for num in nums:
            if num in cache:
                return True
            cache[num] = True
        
        return False
        
        
        
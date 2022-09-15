class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        leftSum = 0
        ssum = sum(nums)
        
        for i, n in enumerate(nums):
            
            # total sum for the right half
            ssum -= n
            
            if leftSum == ssum:
                return i
            
            leftSum += n
            
        return -1
            
        
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def hr1(nums):
            
            rob1, rob2 = 0, 0
            
            for num in nums:
                
                res = max(rob1 + num, rob2)

                rob1 = rob2
                
                rob2 = res
                
            return rob2
        
        arr1, arr2 = nums[1:], nums[:-1]
        
        
        return max(nums[0], hr1(arr1), hr1(arr2))
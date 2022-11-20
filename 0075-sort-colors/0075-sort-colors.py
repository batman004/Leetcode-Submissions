class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n^2) solution
        
#         cnt = {0:0, 1:0, 2:0}
        
#         for x in nums:
#             cnt[x] += 1
            
#         indx = 0
        
#         for v in range(len(cnt)):
#             for c in range(cnt[v]):
#                 nums[indx] = v
#                 indx += 1
                           
    
        l, r = 0, len(nums) - 1
        
        i = 0
        while i <= r:
            
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                
                l += 1
                
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1
                
            i += 1

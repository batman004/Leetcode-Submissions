class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        
        nums.sort()
        
        for i,n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
                
            l, r = i + 1, len(nums) -1 
            
            while l < r:
                three_sum = n + nums[l] + nums[r]
                
                # if sum is value exceeds 0, move to lesser values
                if three_sum > 0:
                    r -= 1
                
                # if sum is less than 0, move towards greater values
                elif three_sum < 0:
                    l += 1
                    
                else:
                    ans.append([n, nums[l], nums[r]])
                    l += 1
                    
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                        
        return ans
                    
                    
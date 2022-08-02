class Solution:
        
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            
            # first check left half of the array
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1 #search right portion
                else:
                    r = mid - 1
            # right sorted array
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1  #search left portion
                    
                else:
                    l = mid + 1
                    
        return -1
                
                
                
            
            
            
            
            
        
        
        
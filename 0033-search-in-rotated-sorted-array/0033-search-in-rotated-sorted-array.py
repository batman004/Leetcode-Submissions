class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # keep track of which part of the array does mid lie in
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            
            mid = l + ((r - l) // 2)
            
            if target == nums[mid]:
                return mid
        
            # left part
            if nums[l] <= nums[mid]:
                
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1 # search in right half
                    
                else:
                    r = mid - 1
            
            # right part        
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                    
                else:
                    # target if greater than middle value and less than 
                    # right most value
                    l = mid + 1
            
        return -1
                    
                
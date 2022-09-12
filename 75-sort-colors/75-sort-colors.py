class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bucket sort 0(n) with extra memory (multiple traversals over nums)
        
        # use partitioning of array
        
        left, right = 0, len(nums) - 1
        # iterator
        i = 0
        
        def swap(i, j):
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            
        while i <= right:
            
            if nums[i] == 0:
                swap(i, left)
                left += 1
                
            if nums[i] == 2:
                swap(i, right)
                right -= 1
                # this is done to keep i at same spot
                i -= 1
            
            i += 1
            
        
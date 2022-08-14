class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        currMin, currMax = 1,1        
        ans = max(nums)

        for num in nums:
            temp = currMax * num
            currMax  = max(currMin * num, currMax * num, num)
            currMin  = min(temp, currMin * num, num) # we use temp here since we need latest max
            ans = max(currMax, ans)
        
            print(ans)
        return ans
            
            
            
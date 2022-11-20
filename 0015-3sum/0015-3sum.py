class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        res = []
        
        nums.sort()
        
        for i,n in enumerate(nums):
            
            # if there are adjacent elements which are same
            # then skip
            # one of them
            
            if i>0 and n == nums[i-1]:
                continue
            # i stores first element of threesum
            
            # basically now using 2-sum algo get the other two
                
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                threeSum = n + nums[l] + nums[r]
                
                if threeSum > 0 :
                    
                    r -= 1
                    
                elif threeSum <0:
                    l += 1
                    
                else:
                    res.append([n, nums[l], nums[r]])
                    # shifting pointers to find next triplet set
                    # we only need to shift left pointer
                    l += 1
                    # basically we dont want duplicate triplets thus 
                    # keep shifting until we donot have adjacent same elements
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
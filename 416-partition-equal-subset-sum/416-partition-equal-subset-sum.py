class Solution:
            
    def canPartition(self, nums: List[int]):
        
        if sum(nums) % 2 !=0 :
            return False
        
        dp = set()
        dp.add(0)
        
        target = sum(nums) // 2
        
        for i in range(len(nums)-1, -1, -1):
            newdp = set()
            for summ in dp:
                newdp.add(summ + nums[i])
                newdp.add(summ)
        

            dp = newdp

        return True if target in dp else False
        
        
        
        
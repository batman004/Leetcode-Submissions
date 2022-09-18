class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def countPallen(l,r):
            local_cntr=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                local_cntr+=1
                l-=1
                r+=1
            return local_cntr
        
        cnt = 0
        
        # odd length pallendromes
        for i in range(len(s)):
            
            cnt += countPallen(i,i)
            
        # even length pallendromes
        for i in range(len(s)):
            
            cnt += countPallen(i,i + 1)
            
               
        return cnt
        
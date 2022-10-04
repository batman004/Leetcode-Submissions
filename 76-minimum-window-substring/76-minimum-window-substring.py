class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # edge case, if t is empty:
        
        if t == "":
            return ""
        
        cntT, window = {}, {}
        
        # keep count of characters which are needed in a substing
        for char in t:
            cntT[char] = 1 + cntT.get(char, 0)
            
        
        have, need = 0, len(cntT)
        # index of left and right ptr to keep track of substring
        # and resLen to keep track of min sub-string
        res, resLen = [-1, -1], float("infinity")
        
        l = 0
        
        # iterate over s to find valid windows
        for r in range(len(s)):
            c = s[r]
            
            window[c] = 1 + window.get(c, 0)
            
            if c in cntT and window[c] == cntT[c]:
                have += 1
                
                # try to minimise substring
                
                while have >= need:
                    if(r - l + 1) < resLen:
                        res = [l, r]
                        resLen = r - l + 1
                        
                    # pop from left of the window
                    window[s[l]] -= 1
                    
                    if s[l] in cntT and window[s[l]] < cntT[s[l]]:
                        have -= 1
                        
                    l += 1
                    
        l, r = res
        
        return s[l : r + 1] if resLen != float("infinity") else ""
                    
            
            
        
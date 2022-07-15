class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map = {}
        
        for ch in s:
            map[ch] = 1 + map.get(ch, 0)
        
        for ch in t:
            if ch in map:
                if map[ch] > 0:
                    map[ch] -= 1
                else:
                    return False
            else:
                return False
        
        return True
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        
        stack = [] # store [element, index]
        
        for i, t in enumerate(temperatures):
            
            # while current element is larged than top of stack
            # keep popping from top of stack
            
            while stack and t > stack[-1][0]:
                
                stackT, stackInd = stack.pop()
                
                res[stackInd] = i - stackInd
                
            stack.append((t,i))
                
                
        return res
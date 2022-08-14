class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0
    
        units = 0
        l, r = 0, len(height) - 1
        
        leftmax, rightmax = height[l], height[r]
        
        while l < r:
            # since we need [height - min(left,right)] and if left < right, we dont need right
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                units += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                units += rightmax - height[r]
                
        return units
        
                
            
        
            
        
            
        
            
            
            
            
            
                       
                       
                      
            
            
        
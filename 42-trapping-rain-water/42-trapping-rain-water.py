class Solution:
    def trap(self, height: List[int]) -> int:
        
#         units = 0
#         l, r = 0, len(height) - 1
        
#         # calc max right for every position
#         maxright = []
#         for i in range(len(height)):
#             rightarr = height[i+1:]
#             if not rightarr:
#                 maxright.append(0)
#             else:      
#                 maxright.append(max(rightarr))
            
#         # calc max left for every position
#         maxleft = []
#         for i in range(1, len(height)+1):
#             leftarr = height[:i-1]
#             if not leftarr:
#                 maxleft.append(0)
#             else:
#                 maxleft.append(max(leftarr))  
                
#         minLR = []
        
#         for i in range(len(maxleft)):
#             minLR.append(min(maxleft[i], maxright[i]))
            
#         # now calculating water units
        
#         for i in range(len(height)):
            
#             units += (height[i] - minLR[i])
            
#         return units


        if not height: return 0
    
        units = 0
        l, r = 0, len(height) - 1
        
        leftmax, rightmax = height[l], height[r]
        
        while l < r:
            
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                units += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                units += rightmax - height[r]
                
        return units
        
                
            
        
            
        
            
        
            
            
            
            
            
                       
                       
                      
            
            
        
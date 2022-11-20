class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        l, r = 0, len(matrix) - 1
        
        while l < r:
            
            for i in range(r - l):
                
                top, bottom = l, r
                
                # save top left value
                topleft = matrix[top][l + i]
                
                # put bottom left value into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # put bottom right value into botom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # put top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # put top left into top right
                matrix[top + i][r] = topleft
                
            r -= 1
            l += 1
                
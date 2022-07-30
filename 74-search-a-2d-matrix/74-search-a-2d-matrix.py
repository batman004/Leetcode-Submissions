class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = 0
        col = len(matrix[row]) - 1
        while (row < len(matrix) and col >= 0):
            if (matrix[row][col] == target):
                return True

            # Target lies in further row
            if (matrix[row][col] < target):
                row += 1

            # Target lies in previous column
            else:
                col -= 1

        return False
        
    
    # TC : O(R + C)
        
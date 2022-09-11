# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def flatten(root):
            if not root:
                return None
            
            leftTail = flatten(root.left)
            #if only right Tail exists no need to flatten
            rightTail = flatten(root.right)
            
            if leftTail:
                leftTail.right = root.right # left tail connected to right root part 
                root.right = root.left # connect root to left half first
                root.left = None
                
            last = rightTail or leftTail or root # order of 'or' is important check rightTail first then left
            return last
                
        flatten(root)
                
            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        
        q = collections.deque([root])
        
        while q:
            
            right = None
            # for each level iterating
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    right = node # represents node left after all nodes on left popped at that level

                    q.append(node.left)
                    q.append(node.right)
                        
            if right:
                res.append(right.val)
                
        return res
                    
                
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        res = []
        
        q = collections.deque()
        q.append(root)
        
        while q:
            # for every level pop from elft of queue and append children from right
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node: 
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # we dont want to append an empty list
            if level:    
                res.append(level)
            
        return res
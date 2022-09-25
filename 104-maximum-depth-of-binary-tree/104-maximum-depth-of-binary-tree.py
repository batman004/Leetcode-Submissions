# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # 1. Recursive DFS
        
        # base case
        if not root:
            return 0
        
        maxLeft = self.maxDepth(root.left)
        maxRight = self.maxDepth(root.right)
        
        return 1 + max(maxLeft, maxRight)
    
    
        # 2. BFS iterative (Level-order-traversal)
        
#         if not root:
#             return 0
        
#         # use deque
#         dq = deque([root])
#         level = 0
        
#         while dq:
            
#             for i in range(len(dq)):
#                 node = dq.popleft() # get root node at that particular level
#                 if node.left:
#                     dq.append(node.left)
#                 if node.right:
#                     dq.append(node.right)
                    
#             level += 1
            
#         return level


        # 3. DFS itertative
    
#         stack = [[root, 1]]
#         res = 0
        
#         while stack:
#             node, depth = stack.pop()
            
#             if node:
#                 res = max(res, depth)
#                 stack.append([node.left, depth + 1])
#                 stack.append([node.right, depth + 1])
        
#         return res
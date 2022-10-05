class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        
        q = collections.deque()
        
        l = r = 0
        
        # while right ptr does not reach end of array
        while r < len(nums):
            
            # pop from queue while top of queue is less than element to be added
            while q and nums[q[-1]] < nums[r]:
                q.pop()
                
            # now append into queue
            q.append(r)
            
            # if left most element in queue is not in current window remove it
            if l > q[0]:
                q.popleft()
                
            if r + 1 >= k:
                output.append(nums[q[0]])
                l +=1
                
            r +=1
            
        return output
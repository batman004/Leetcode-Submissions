class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_to_count = {}
        
        freq = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            num_to_count[num] = 1 + num_to_count.get(num,0)
            
        
        for key,val in num_to_count.items():
            freq[val].append(key)

        
        res = []
        
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        
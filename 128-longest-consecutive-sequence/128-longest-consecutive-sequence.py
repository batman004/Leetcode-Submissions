class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        
        # init longest subsequence length to 0
        longest = 0
        
        for num in nums:
            
            # checking start of sequence
            if(num - 1) not in numSet:
                # length of this particular sequence
                length = 0
                
                # if the next number in sequence exists
                while(num + length) in numSet:
                    length +=1
                longest = max(longest, length)
                
        return longest
                
        
        
        
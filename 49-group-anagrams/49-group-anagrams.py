class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}  
        
        for word in strs:
            
            # get sorted alphabets as keys
            sortedWord = tuple(sorted(word)) 

            # map words with same alphabets to the words
            if not result.get(sortedWord): 
                result[sortedWord] = [word]
                
            else:
                result[sortedWord].append(word)   

        return result.values() 
        
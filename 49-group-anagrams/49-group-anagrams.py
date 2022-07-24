class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        char_count_to_words = defaultdict(list)
        
        for word in strs:
            
            chars = [0] * 26 # for all alphabets
            
            for char in word:
                chars[ord(char) - ord("a")] += 1
                
            char_count_to_words[tuple(chars)].append(word)
            
            
        return char_count_to_words.values()
        
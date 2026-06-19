from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Create a dictionary where the default value is an empty list
        anagram_map = defaultdict(list)
        
        for word in strs:
            # 1. Sort the characters of the word and join them back into a string
            # (e.g., 'eat' becomes 'aet')
            sorted_word = "".join(sorted(word))
            
            # 2. Add the original word to the list for this sorted key
            anagram_map[sorted_word].append(word)
            
        # 3. Return just the grouped lists (the values of the dictionary)
        return list(anagram_map.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        zero = defaultdict(list)

        for s in strs:

            sorted_s = "".join(sorted(s))
            
            
                
            zero[sorted_s].append(s)

        return list(zero.values())    

        
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #mapping character count to list of anagrams
        res = defaultdict(list)
        #goes through every single character in each string
        for s in strs:
            count = [0] * 26 # a...z
            for char in s:
                #ord generates ascii values
                count[ord(char) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()
                
                
        
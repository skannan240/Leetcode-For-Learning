class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #storage = {}
        #length = 0
        #counter = 0
        #for i in range(len(s)):
            #if s[i] not in storage:
                #storage[counter] = s[i]
                #counter += 1
                #length += 1
            #else:
                #return length
        #return length
        
        charSet = set()
        l = 0
        result = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)
        
        return result
            
            
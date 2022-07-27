class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        result = 0
        count = {}
        for r in range(len(s)):
            #for the character at position r we are going to increment the 
            #count of it. 1 + whatever the count currently was and if character
            #doesn't exist it returns default value of 0
            count[s[r]] = 1 + count.get(s[r],0)
            
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        
        return result
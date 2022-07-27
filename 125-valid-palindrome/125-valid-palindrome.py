class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''.join(filter(str.isalnum, s))
        if newS[::-1].lower() == newS.lower():
            return True
        else:
            return False
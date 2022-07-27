class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}
        
        if len(s) % 2 != 0:
            return False
        
        
        for c in s:
            #check if character is closing parenthesis
            if c in closeToOpen:
                #stack[-1] is llast value we added to stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        #only return true if stack is empty
        return True if not stack else False
            
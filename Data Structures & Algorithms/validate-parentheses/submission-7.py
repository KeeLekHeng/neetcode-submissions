class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2 != 0:
            return False
        
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if not stack:
                    return False
                    
                if stack and c == "]" and stack.pop() != "[":
                    return False
                elif stack and c == "}" and stack.pop() != "{":
                    return False
                elif stack and c == ")" and stack.pop() != "(":
                    return False
        
        #we want stack to be empty at the end
        return not stack 

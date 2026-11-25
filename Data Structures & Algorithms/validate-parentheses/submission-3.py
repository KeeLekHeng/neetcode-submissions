class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        openings = set(["(", "{", "["])

        for c in s:
            if c in openings:
                stack.append(c)
            else:
                if not stack:
                    return False
                elif c == ")" and stack[-1] != "(":
                    return False
                    
                elif c == "]" and stack[-1] != "[":
                    return False

                elif c == "}" and stack[-1] != "{":
                    return False
                stack.pop()

        return not stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c not in ["+", "-", "/", "*"]:
                stack.append(int(c))
            else:
                val = 0
                a = int(stack.pop())
                b = int(stack.pop())
                if c == "+":
                    val = a + b
                elif c == "*":
                    val = a * b
                elif c == "-":
                    val = b - a
                elif c == "/":
                    val = b / a

                stack.append(int(val))
            
        return stack[-1]
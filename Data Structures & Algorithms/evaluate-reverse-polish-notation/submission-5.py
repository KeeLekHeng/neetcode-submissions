class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for i in range(len(tokens)):
            if tokens[i].lstrip("-").isdigit():
                stack.append(tokens[i])
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if tokens[i] == "/":
                    res = b / a
                elif tokens[i] == "*":
                    res = a * b
                elif tokens[i] == "+":
                    res = a + b
                elif tokens[i] == "-":
                    res = b - a
                stack.append(res)
        #only one digit and is answer
        if len(stack) == 1:
            res = int(stack.pop())
        return res
                
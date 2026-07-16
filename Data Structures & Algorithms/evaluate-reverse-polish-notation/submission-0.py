class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i, x in enumerate(tokens):
            if x not in "+-*/":
                stack.append(int(x))
            else:
                a = stack.pop()
                b = stack.pop()
                if x == '+':
                    stack.append(a + b)
                elif x == '-':
                    stack.append(b - a)
                elif x == '*':
                    stack.append(a * b)
                elif x == '/':
                    stack.append(int(b / a))
        return stack[0]
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0
        for ch in tokens:
            if ch == "+":
                stack.append(stack.pop() + stack.pop())
            elif ch == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif ch == "*":
                stack.append(stack.pop() * stack.pop())
            elif ch == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 / n1))
            else:
                stack.append(int(ch))
            print(stack)
        return stack[0]
# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack  = []

        for i in tokens:
            if i != "+" and i != "-" and i != "*" and i != "/":
                stack.append(int(i))
            else:
                if len(stack) >= 2:
                    if i == "+":
                        result = stack[-2] + stack[-1]
                    elif i == "-":
                        result = stack[-2] - stack[-1]
                    elif i == "*":
                        result = stack[-2] * stack[-1]
                    elif i == "/":
                        result = int(stack[-2] / stack[-1])
                        
                    stack.pop()
                    stack.pop()
                    stack.append(result)

        return stack[0]
        
        ## 
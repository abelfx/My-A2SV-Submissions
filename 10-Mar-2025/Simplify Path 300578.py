# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split("/")
        stack = []
        result = ""

        for i in lst:
            if i == "..":
                if stack:
                    stack.pop()
            elif i == "." or i == "":
                continue
            else:
                stack.append(i)


        if len(stack) == 0:
            result += "/"
        else:
            for i in stack:
                if i != "":
                    result += "/"
                    result += i
        
        return result
        
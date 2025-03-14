# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = []

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char) 
            elif char == '[':
                stack.append((current_str, current_num))
                current_str, current_num = [], 0  
            elif char == ']':
                last_str, num = stack.pop()
                current_str = last_str + current_str * num 
            else:
                current_str.append(char) 

        return ''.join(current_str)  
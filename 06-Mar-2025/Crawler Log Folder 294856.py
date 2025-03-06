# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for folder in logs:
            if folder == "../":
                if len(stack) > 0:
                    stack.pop()   
            else:
                if folder == "./":
                    continue
                stack.append(folder)
        
        return len(stack)
        
        
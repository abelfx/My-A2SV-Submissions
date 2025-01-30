# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:

        result = ""
        for i in range(len(command)):
            if(command[i] == "G"):
                result += "G"
            elif(command[i] == "(" and command[i+1] == ")"):
                result += "o"
            elif(command[i] == "(" and command[i + 1] == "a" and command[i + 2] == "l" and command[i+3] == ")"):
                result += "al"

        
        return result
        
        
            
        
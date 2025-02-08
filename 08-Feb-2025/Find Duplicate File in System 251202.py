# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

         dict = defaultdict(list)

         for path in paths:
            path = path.split()
            folder = path[0]

            for v in path[1:]:
                name, content = v.split(".txt")
                dict[content].append((folder, name))
        
         output = []

         for values in dict.values():
            if len(values) > 1:
                temp = []
                for folder, name in values:
                    temp.append((folder + "/" + name  + ".txt").replace(" ", ""))
                
                output.append(temp)

         return output

        
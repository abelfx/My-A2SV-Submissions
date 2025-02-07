# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        aux_s = [""] * len(s)   # 

        for i in range(len(indices)):  
            aux_s[indices[i]] = s[i]        

        return "".join(aux_s)
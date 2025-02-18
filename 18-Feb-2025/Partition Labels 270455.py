# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # store the last occurance in some data structure
        # after we see the the first occurance do the max last occurance avaliable 
             # abacbaca defegde
        # when indx = largest last occurance indx append it to the result
        # use some sort of buffer where you reduce the last partition length
        # buffer = indx + 1

        dict = {char: indx for indx, char in enumerate(s)}

        last_elem = float("-inf") 
        buffer = 0

        result = []
        for indx in range(len(s)):
            last_elem = max(last_elem, dict[s[indx]])

            if indx == last_elem:
                result.append(indx - buffer + 1)
                buffer = indx + 1
        
        return result


   


        

        
        
    



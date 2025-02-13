# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        i = 0
        j = len(people) - 1
        result = 0

        while (i <= j):
            if people[i] + people[j] <= limit:
                i +=1
            j -= 1
            result +=1
        
        return result


        

            


        
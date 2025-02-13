# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        i = 0
        j = 0

        counter = 0
        while (i < len(seats)):
            if seats[i] != students[i]:
                while(seats[i] > students[i]):
                    students[i] += 1
                    counter += 1
                while(seats[i] < students[i]):
                    students[i] -= 1
                    counter += 1
            i+=1

        
        return counter
                


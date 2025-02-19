# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        intersections = []

        first_idx = 0
        second_idx = 0

        while(first_idx < len(firstList) and second_idx < len(secondList)):
            maxx = max(firstList[first_idx][0], secondList[second_idx][0])
            minn = min(firstList[first_idx][1], secondList[second_idx][1])

            if maxx <= minn:
                intersections.append([maxx, minn])

            if firstList[first_idx][1] < secondList[second_idx][1]:
                first_idx += 1
            else:
                second_idx += 1
        
        return intersections

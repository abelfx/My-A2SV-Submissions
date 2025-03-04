# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        lst = []
        total_cost = 0

        for cost in costs:
            lst.append(cost[1] - cost[0])
            total_cost += cost[0]

        lst.sort()

        print(total_cost)
        for i in range(len(lst) // 2):
            total_cost += lst[i]
        
        return total_cost
        
# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        queue = deque()
        order = []

        for need, needed in prerequisites:
            graph[needed].append(need)
            incoming[need] += 1
        
        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) != numCourses:
            return []
        
        return order




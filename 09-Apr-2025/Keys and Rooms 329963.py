# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # visited = set()
        # stack = [0]
        # check if rooms in the stack are visited or not?
        # put them in the visited set
        # then remove from the stack

        visited = set()
        stack = [0]

        while stack:
            room = stack.pop()
            for i in rooms[room]:
                if i not in visited:
                    stack.append(i)
            visited.add(room)
        
        print(visited)
        return len(visited) == len(rooms)
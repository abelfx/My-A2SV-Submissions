# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.deq = deque()
    def ping(self, t: int) -> int:

        self.deq.append(t)
        while self.deq[0] < t-3000:
            self.deq.popleft()
        
        return len(self.deq)




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
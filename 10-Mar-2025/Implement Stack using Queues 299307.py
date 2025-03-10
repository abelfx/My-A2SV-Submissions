# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.q = deque()
    def push(self, x: int) -> None:
        self.q.append(x)
    

    def pop(self) -> int:
        if self.q:
            return self.q.pop()

        

    def top(self) -> int:
        if self.q:
            return self.q[-1]
       

    def empty(self) -> bool:
        if not self.q:
            return True
        return False
    

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
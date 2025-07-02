# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.stack1)-1, -1, -1):
            self.stack2.append(self.stack1[i])
        
        self.stack1.clear()
        popped = self.stack2.pop()

        for i in range(len(self.stack2)-1, -1, -1):
            self.stack1.append(self.stack2[i])
        self.stack2.clear()
        return popped
        

    def peek(self) -> int:
        return self.stack1[0]
        

    def empty(self) -> bool:
        return len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
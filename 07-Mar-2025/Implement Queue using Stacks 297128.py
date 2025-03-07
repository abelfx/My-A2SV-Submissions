# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stackA = []
        self.stackB = []
        
    def push(self, x: int) -> None:
        self.stackA.append(x)
        

    def pop(self) -> int:
        while self.stackA:
            self.stackB.append(self.stackA.pop())
        poped = self.stackB.pop()

        while self.stackB:
            self.stackA.append(self.stackB.pop())
        
        return poped

    def peek(self) -> int:
        return self.stackA[0]
        

    def empty(self) -> bool:
        if self.stackA:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
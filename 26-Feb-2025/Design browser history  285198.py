# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.start = ListNode(homepage)

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        self.start.next = new_node
        new_node.prev = self.start
        self.start = self.start.next
        

    def back(self, steps: int) -> str:
        while self.start.prev and steps > 0:
            self.start = self.start.prev
            steps -= 1
        return self.start.val
        

    def forward(self, steps: int) -> str:
        while self.start.next and steps > 0:
            self.start = self.start.next
            steps -= 1
        return self.start.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
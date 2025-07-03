# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return 
        inter = []
        while head:
            inter.append(head.val)
            head = head.next

       
        reversed = ListNode(inter[len(inter) - 1])

        current = reversed
        for i in range(len(inter)-2, -1, -1):
            current.next = ListNode(inter[i])
            current = current.next
        
        return reversed

        
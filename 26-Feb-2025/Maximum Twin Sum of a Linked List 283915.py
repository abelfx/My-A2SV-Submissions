# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        
        maxx = float("-inf")

        for i in range(int(len(lst) / 2)):
            maxx = max(maxx, lst[i] + lst[len(lst) - i - 1])
        
        return maxx
        
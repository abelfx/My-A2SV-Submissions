# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        res = []

        current = head

        while current:
            res.append(current.val)
            current = current.next
        
        res.sort()

        head1 = ListNode(res[0])
        current1 = head1
        for i in range(1, len(res)):
            current1.next = ListNode(res[i])
            current1 = current1.next
        
        return head1


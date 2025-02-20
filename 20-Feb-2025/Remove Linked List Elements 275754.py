# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_node = ListNode(0, head)
        current = new_node

        while(current):
            if(current.next and current.next.val == val):
                current.next = current.next.next
            else:
                current = current.next
        
        return new_node.next
# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_node = ListNode(0, head)
        curr = new_node
        prev = new_node
      
        length = 0
        while curr:
            length += 1
            curr = curr.next

        to_delete = length - n
   
        counter = 1
        while counter < length:
            if counter == to_delete:
                prev.next = prev.next.next
            else:
                prev = prev.next
            counter += 1
        
        return new_node.next
            
        



        
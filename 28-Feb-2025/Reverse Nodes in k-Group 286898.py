# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        
        
        j = k - 1

        while j < len(result):
            i = j-k+1
            l = j

            while i < l:
                temp = result[i]
                result[i] = result[l]
                result[l] = temp
                i += 1
                l -= 1     
            j = j + k   
        
        new_node = ListNode(0)
        dummy = new_node

        for num in result:
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        return new_node.next
            

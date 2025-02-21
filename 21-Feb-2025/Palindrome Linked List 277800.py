# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        lst = []

        while current:
            lst.append(current.val)
            current = current.next
        
        left = 0
        right = len(lst) - 1

        while left < right:
            if lst[left] != lst[right]:
                return False
            left += 1
            right -= 1
        
        return True

# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        
        left = 1
        right = n

        while (left <= right):
            mid = (left + right) // 2
            if isBadVersion(mid) == False and isBadVersion(mid+1) == True:
                return mid+1
            elif isBadVersion(mid) == False and isBadVersion(mid+1) == False:
                left = mid+1
            elif isBadVersion(mid) == True and isBadVersion(mid-1) == True:
                right = mid-1
            elif isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid
        
        return -1


        
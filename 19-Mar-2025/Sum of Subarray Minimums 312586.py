# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = [0] * len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            j = 0
            if stack:
                j = stack[-1]
            else:
                j = -1
            
            res[i] = res[j] + (i - j) * arr[i]

            stack.append(i)
        
        return sum(res) % ((10**9)+7)
                

        
        
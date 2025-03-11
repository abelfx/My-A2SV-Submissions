# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = factorial(n)

        count = 0
        while num % 10 == 0:
            num = num // 10
            count += 1
        
        return count


    def factorial(n):
        if n == 1:
            return 1
        fact = n * factorial(n - 1)
        return fact
        
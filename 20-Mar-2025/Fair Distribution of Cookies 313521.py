# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        fairness = float("inf")

        def fair(children, i):
            nonlocal fairness
            if i == len(cookies):
                fairness = min(fairness, max(children))
                return

            for j in range(k):
                if cookies[i] + children[j] <= fairness:
                    children[j] += cookies[i]
                    fair(children, i+1)
                    children[j] -= cookies[i]
        
        fair(children, 0)
        return fairness            


            


        
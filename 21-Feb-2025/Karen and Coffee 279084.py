# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split())

MAX_N = 200001  
coverage = [0] * (MAX_N + 1)


for _ in range(n):
    l, r = map(int, input().split())
    coverage[l] += 1
    coverage[r + 1] -= 1  

active_recipes = [0] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    active_recipes[i] = active_recipes[i - 1] + coverage[i]

valid_prefix = [0] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    valid_prefix[i] = valid_prefix[i - 1] + (1 if active_recipes[i] >= k else 0)


for _ in range(q):
    l, r = map(int, input().split())
    print(valid_prefix[r] - valid_prefix[l - 1])

# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

t = int(input())
for _ in range(t):
n, k = map(int, input().split()) 
pos = list(map(int, input().split())) temp = list(map(int, input().split()))
all = [float('inf')] * n  
for i in range(k):  
    all[pos[i] - 1] = temp[i]  

forward = [float('inf')] * n  
forward[0] = all[0]  
for i in range(1, n):  
    forward[i] = min(forward[i - 1] + 1, all[i])  

backward = [float('inf')] * n  
backward[-1] = all[-1]  
for i in range(n - 2, -1, -1):  
    backward[i] = min(backward[i + 1] + 1, all[i])  

result = [min(forward[i], backward[i]) for i in range(n)]  
print(*result)  
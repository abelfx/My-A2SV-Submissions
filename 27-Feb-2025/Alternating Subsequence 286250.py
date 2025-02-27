# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    cur_max = lst[0]

    result = 0
    i = 1
    while i < n:
        if (cur_max > 0 and lst[i] > 0) or (cur_max < 0 and lst[i] < 0):
            cur_max = max(cur_max, lst[i])
        else:
            result += cur_max
            cur_max = lst[i]
        
        i += 1
    
    result += cur_max
    
    print(result)



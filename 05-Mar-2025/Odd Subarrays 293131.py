# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    count = 0

    i = 0
    j = 1

    while j < len(lst):
        if lst[i] > lst[j]:
            i += 2
            j += 2
            count += 1
        else:
            i += 1
            j += 1
    
    print(count)
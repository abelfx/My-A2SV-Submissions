# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    count = Counter(arr)

    options = set(count.values())
    min_deletions = float('inf')
    
    #c is always in range 1 to n
    for c in range(1, n + 1):
        if c not in options:
            continue

        deletions = 0
        for num in count:
            if count[num] < c:
                deletions += count[num]
            else:
                deletions += count[num] - c
        
        min_deletions = min(min_deletions, deletions)
    
    print(min_deletions)
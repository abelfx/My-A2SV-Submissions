# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    left_counter = Counter()
    right_counter = Counter(s)

    maxx = float("-inf")
    for c in s:
        left_counter[c] += 1
        right_counter[c] -= 1

        if right_counter[c] == 0:
            del right_counter[c]
        
        maxx = max(maxx, len(left_counter) + len(right_counter))
    
    print(maxx)




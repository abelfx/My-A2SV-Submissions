# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import Counter

n, k = map(int, input().split())
lst = list(map(int, input().split()))

i = 0
j = k-1

dict = Counter(lst[i:j+1])

left = 0
right = 0

maxx = float("-inf")
while j < len(lst):

    if len(dict) <= k:
        if maxx < j - i:
            maxx = j - i
            left = i+1
            right = j+1

        j += 1
        if j < len(lst):
            dict[lst[j]] += 1

    else:
        dict[lst[i]] -= 1
        if dict[lst[i]] == 0:
            del dict[lst[i]]
        i += 1
print(left, right)


# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

import sys
from math import ceil


def input():
    return sys.stdin.readline().strip()


def earliest_decision_point(s):
    length = len(s)
    ans = length

    def recurse(index, cur1, cur2):
        nonlocal ans
        if index >= length:
            return

        remaining = length - index
        if index % 2:
            if cur2 + ceil(remaining / 2) < cur1 or cur1 + remaining // 2 < cur2:
                ans = min(ans, index)
                return
            if s[index] == "1":
                recurse(index + 1, cur1, cur2 + 1)
            elif s[index] == "0":
                recurse(index + 1, cur1, cur2)
            else:
                recurse(index + 1, cur1, cur2 + 1)
                recurse(index + 1, cur1, cur2)
        else:
            if cur1 + ceil(remaining / 2) < cur2 or cur2 + remaining // 2 < cur1:
                ans = min(ans, index)
                return
            if s[index] == "1":
                recurse(index + 1, cur1 + 1, cur2)
            elif s[index] == "0":
                recurse(index + 1, cur1, cur2)
            else:
                recurse(index + 1, cur1 + 1, cur2)
                recurse(index + 1, cur1, cur2)

    recurse(0, 0, 0)
    return ans


t = int(input().strip())
for _ in range(t):
    s = input().strip()
    print(earliest_decision_point(s))
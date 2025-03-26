# Problem: The Meeting Place Cannot Be Changed - https://codeforces.com/problemset/problem/780/B

t = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

right = max(lst1)
left = min(lst1)
precision = 0.000001


def max_time(target):
    maxx_time = 0
    for idx, pos in enumerate(lst1):
        cur_time = abs(pos - target) / lst2[idx]
        maxx_time = max(maxx_time, cur_time)

    return maxx_time

ans = max_time(left)

min_sec = float("inf")

while right - left > precision:
    mid = (left + right) / 2
    time_left = max_time(mid - precision)
    time_right = max_time(mid + precision)

    if time_left < time_right:
        ans = time_left
        right = mid - precision
    else:
        ans = time_right
        left = mid + precision

print(ans)


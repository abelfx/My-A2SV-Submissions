# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())

lst = list(map(int, input().split()))


left = 0
max_len = 0
cur_sum = 0

for right in range(len(lst)):
    cur_sum += lst[right]
    while(cur_sum > s):
        cur_sum -= lst[left]
        left += 1

    max_len = max(max_len, right-left + 1)

print(max_len)



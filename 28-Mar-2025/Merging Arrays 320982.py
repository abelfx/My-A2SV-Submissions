# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, (input().split()))

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

result = lst1 + lst2

print(*sorted(result))
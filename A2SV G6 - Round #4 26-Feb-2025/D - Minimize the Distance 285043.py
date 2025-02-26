# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

t = int(input())
lst = list(map(int, input().split()))

lst.sort()
print(lst[(t - 1)// 2])
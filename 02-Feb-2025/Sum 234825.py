# Problem: Sum - https://codeforces.com/contest/1742/problem/A

t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    lst = [a, b, c]

    lst.sort()
    length = len(lst)
    sums = 0

    for i in range(length):
        if(i != length - 1):
            sums += lst[i]

    if sums == lst[length - 1]:
        print('YES')
    else:
        print("NO")

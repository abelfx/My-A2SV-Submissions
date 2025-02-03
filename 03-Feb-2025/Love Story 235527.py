# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t = int(input())

main = "codeforces"

difference = 0
for i in range(t):
    s = input()
    for i in range(len(main)):
        if(main[i] != s[i]):
            difference +=1
    print(difference)
    difference = 0
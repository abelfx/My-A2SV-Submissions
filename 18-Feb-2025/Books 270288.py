# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
books = list(map(int, input().split()))

left = 0
prefix_sum = 0
counter = 0

maxx = float("-inf")
for right in range(len(books)):
    prefix_sum += books[right]

    while(prefix_sum > t):
        prefix_sum -= books[left]
        left += 1
        counter -= 1
    
    counter += 1
    right += 1

    maxx = max(maxx, counter)

print(maxx)

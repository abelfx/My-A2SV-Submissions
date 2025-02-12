# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

f, s = map(int, input().split())

first_arr = list(map(int, input().split()))
second_arr = list(map(int, input().split()))

counter = 0
result = []
j = 0
for i in second_arr:
    while(j < len(first_arr)):
        if(i > first_arr[j]):
            counter += 1
            j += 1
        else:
            break
    
    result.append(counter)

print(*result)


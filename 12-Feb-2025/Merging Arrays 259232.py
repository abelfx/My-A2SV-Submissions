# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

f_t, s_t = map(int, input().split())

first_arr = list(map(int, input().split()))
second_arr = list(map(int, input().split()))

i = 0
j = 0

result = []
while (i < len(first_arr) and j < len(second_arr)):
    if(first_arr[i] < second_arr[j]):
        result.append(first_arr[i])
        i += 1
    else:
        result.append(second_arr[j])
        j+= 1

while i < len(first_arr):
    result.append(first_arr[i])
    i += 1

while j < len(second_arr):
    result.append(second_arr[j])
    j += 1

print(*result)
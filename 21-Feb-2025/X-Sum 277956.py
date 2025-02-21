# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, m, grid))

results = []
for case in test_cases:
    n, m, grid = case
    
    main_diag = {}
    anti_diag = {}

    for i in range(n):
        for j in range(m):
            main_diag[i + j] = main_diag.get(i + j, 0) + grid[i][j]
            anti_diag[i - j] = anti_diag.get(i - j, 0) + grid[i][j]
    
    max_sum = 0

    for i in range(n):
        for j in range(m):
            bishop_sum = main_diag[i + j] + anti_diag[i - j] - grid[i][j]
            max_sum = max(max_sum, bishop_sum)

    results.append(max_sum)

for result in results:
    print(result)

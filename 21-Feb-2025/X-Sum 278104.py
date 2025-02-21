# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t = int(input())
test_case = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    test_case.append((n, m, grid))


results = []
for case in test_case:
    n, m, grid = case
    
    main_diagonal = {}
    anti_diagonal = {}

    for i in range(n):
        for j in range(m):
            main_diagonal[i + j] = main_diagonal.get(i + j, 0) + grid[i][j]
            anti_diagonal[i - j] = anti_diagonal.get(i - j, 0) + grid[i][j]
    
    maxx_sum = 0

    for i in range(n):
        for j in range(m):
             cur_sum = main_diagonal[i + j] + anti_diagonal[i - j] - grid[i][j]
             maxx_sum = max(maxx_sum, cur_sum)

    print(maxx_sum)

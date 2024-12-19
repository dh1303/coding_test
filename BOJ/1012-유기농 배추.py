import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    m, n, k = map(lambda x: int(x), sys.stdin.readline().strip().split())
    arrive = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(lambda x: int(x), sys.stdin.readline().strip().split())
        arrive[y][x] = 1
    
    result = 0

    def dfs(y, x):
        arrive[y][x] = 0

        if  x+1 < m and arrive[y][x+1]:
            dfs(y, x+1)
        if  y+1 < n and arrive[y+1][x]:
            dfs(y+1, x)
        if  x-1 >= 0 and arrive[y][x-1]:
            dfs(y, x-1)
        if  y-1 >= 0 and arrive[y-1][x]:
            dfs(y-1, x)
        

    for j in range(n):
        for i in range(m):
            if arrive[j][i]:
                result += 1
                dfs(j, i)

    print(result)
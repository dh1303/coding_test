import sys
n, m = map(int, sys.stdin.readline().split(' '))

numbers = [[0 for _ in range(n + 1)]]
prefix_sum = [[0 for _ in range(n + 1)]]

result = 0

for i in range(n):
    numbers.append([0] + list(map(int, sys.stdin.readline().split(' '))))

for i in range(1, n + 1):
    prefix_sum.append([0])
    for j in range(1, n + 1):
        prefix_sum[i].append(numbers[i][j] + prefix_sum[i-1][j]
                     + prefix_sum[i][j-1] - prefix_sum[i-1][j-1])
        

for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split(' '))
    result = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
    print(result)
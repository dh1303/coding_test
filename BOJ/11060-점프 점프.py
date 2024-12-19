import sys

N = int(sys.stdin.readline())

A = [ int(x) for x in sys.stdin.readline().split() ]

dp = [ sys.maxsize for _ in range(len(A))]

def solution(x, y):
    if x >= N:
        return 0

    if dp[x] <= y:
        return 0

    dp[x] = y

    for i in range(A[x]):
        solution(x+i+1, y+1)

solution(0, 0)

if dp[-1] == sys.maxsize:
    print(-1)
else:
    print(dp[-1])

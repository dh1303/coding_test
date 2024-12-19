import sys
N, Q = map(lambda x: int(x), sys.stdin.readline().split(' '))

vote = [0 for _ in range(N+2)]

check = True
max = 0
sum = 0

for i in range(Q):
    number, x, y = map(int, sys.stdin.readline().split(' '))
    if number == 1:
        vote[y] += x
        if y != N+1:
            sum += x
            if max < vote[y]:
                max = vote[y]
    else:
        if max >= vote[N+1] + x or (sum+y) / N > vote[N+1] + x - 1:
            print("NO")
        else:
            print("YES")
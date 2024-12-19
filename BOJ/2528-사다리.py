import sys

N, L = map(int, sys.stdin.readline().split(' '))

time = 0
floor = 0

stick = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]

while floor < N-1:
    if stick[floor][1] == stick[floor+1][1]:
        floor += 1
    elif stick[floor][0] + stick[floor+1][0] + (time * 2) >= L:
        floor += 1
    else:
        time += 1

print(time)
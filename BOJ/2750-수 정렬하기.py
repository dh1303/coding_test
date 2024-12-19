import sys

N = int(sys.stdin.readline())

li = []

for _ in range(N):
    li.append(int(sys.stdin.readline()))

for i in range(1, N):
    for j in range(N-i):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]


for l in li:
    print(l)
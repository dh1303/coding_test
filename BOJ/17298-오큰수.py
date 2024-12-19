import sys
N = int(sys.stdin.readline())

A = [ int(x) for x in sys.stdin.readline().split() ]

stack = []

result = [ 0 for _ in range(N) ]

for idx, a in enumerate(A):
    while stack:
        if a > stack[-1][0]:
            e = stack.pop()
            result[e[1]] = a
        else:
            break
    stack.append((a, idx))

if stack:
    for _, idx in stack:
        result[idx] = -1

for r in result:
    print(r, end=" ")
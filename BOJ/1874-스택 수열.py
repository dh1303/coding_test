import sys
N = int(sys.stdin.readline())

sequence = []

stack = []

result = []

idx = 0

for _ in range(N):
    n = int(sys.stdin.readline())
    sequence.append(n)


for i in range(1, N+1):
    stack.append(i)
    result.append('+')
    
    while stack and stack[-1] == sequence[idx]:
        stack.pop()
        idx += 1
        result.append('-')

if idx != N:
    print('NO')
    exit()

for r in result:
    print(r)
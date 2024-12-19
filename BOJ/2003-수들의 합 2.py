import sys

N, M = map(int, sys.stdin.readline().split())

numbers = [ int(x) for x in sys.stdin.readline().split() ]

prefix_sum = [0]

a = 0
b = 1

temp = 0

result = 0

for number in numbers:
    temp += number
    prefix_sum.append(temp)

while b <= N:
    target = prefix_sum[b] - prefix_sum[a]

    if target > M:
        a += 1
    elif target < M:
        b += 1
    else:
        result += 1
        b += 1


print(result)
